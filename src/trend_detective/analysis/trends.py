"""Reusable trend and significance statistics for xarray time series."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import xarray as xr
from scipy.stats import linregress, norm, theilslopes


@dataclass(frozen=True)
class TrendResult:
    """Summary of a monotonic trend estimate."""

    slope: float
    p_value: float
    significant: bool
    confidence_interval: tuple[float, float]
    n_obs: int

    @property
    def ci_low(self) -> float:
        return self.confidence_interval[0]

    @property
    def ci_high(self) -> float:
        return self.confidence_interval[1]


def _clean_values(values: Any) -> np.ndarray:
    array = np.asarray(values, dtype=float).reshape(-1)
    return array[np.isfinite(array)]


def _clean_with_positions(values: Any) -> tuple[np.ndarray, np.ndarray]:
    array = np.asarray(values, dtype=float).reshape(-1)
    mask = np.isfinite(array)
    return array[mask], np.flatnonzero(mask).astype(float)


def mann_kendall_test(values: Any) -> tuple[float, float]:
    """Return the Mann-Kendall S statistic and two-sided normal p-value.

    Missing and non-finite values are removed. The implementation applies the
    tie-corrected variance and continuity correction used by the classic
    seasonal-free Mann-Kendall test.
    """

    clean = _clean_values(values)
    n = clean.size
    if n < 3:
        return float("nan"), float("nan")

    differences = clean[np.newaxis, :] - clean[:, np.newaxis]
    upper = differences[np.triu_indices(n, k=1)]
    statistic = float(np.sign(upper).sum())

    _, counts = np.unique(clean, return_counts=True)
    tie_term = float(np.sum(counts * (counts - 1) * (2 * counts + 5)))
    variance = (n * (n - 1) * (2 * n + 5) - tie_term) / 18.0
    if variance == 0:
        return statistic, 1.0

    if statistic > 0:
        z = (statistic - 1.0) / np.sqrt(variance)
    elif statistic < 0:
        z = (statistic + 1.0) / np.sqrt(variance)
    else:
        z = 0.0
    p_value = float(2.0 * norm.sf(abs(z)))
    return statistic, p_value


def _theil_sen_slope_with_x(values: Any) -> tuple[float, tuple[float, float]]:
    clean, x = _clean_with_positions(values)
    if clean.size < 2:
        return float("nan"), (float("nan"), float("nan"))
    result = theilslopes(clean, x, alpha=0.95)
    return float(result.slope), (float(result.low_slope), float(result.high_slope))


def theil_sen_slope(values: Any) -> tuple[float, tuple[float, float]]:
    """Return Theil-Sen slope and its 95% confidence interval."""

    return _theil_sen_slope_with_x(values)


def linear_regression(values: Any) -> dict[str, float]:
    """Fit ordinary least-squares regression against observation order."""

    clean = _clean_values(values)
    if clean.size < 2:
        return {"slope": float("nan"), "intercept": float("nan"), "p_value": float("nan"), "r_value": float("nan")}
    fit = linregress(np.arange(clean.size, dtype=float), clean)
    return {
        "slope": float(fit.slope),
        "intercept": float(fit.intercept),
        "p_value": float(fit.pvalue),
        "r_value": float(fit.rvalue),
    }


def analyze_series(values: Any, times: Any | None = None, alpha: float = 0.05) -> TrendResult:
    """Estimate a robust monotonic trend for one time series.

    ``times`` is accepted for API compatibility and future irregular-time
    support. The current slope is expressed per valid observation, which keeps
    the result stable for gridded products with missing timestamps.
    """

    del times
    clean = _clean_values(values)
    slope, confidence_interval = _theil_sen_slope_with_x(values)
    _, p_value = mann_kendall_test(clean)
    return TrendResult(
        slope=slope,
        p_value=p_value,
        significant=bool(np.isfinite(p_value) and p_value < alpha),
        confidence_interval=confidence_interval,
        n_obs=int(clean.size),
    )


def _analyze_tuple(values: np.ndarray, alpha: float) -> tuple[float, float, bool, float, float, int]:
    result = analyze_series(values, alpha=alpha)
    return (
        result.slope,
        result.p_value,
        result.significant,
        result.ci_low,
        result.ci_high,
        result.n_obs,
    )


def analyze_dataarray(data: xr.DataArray, dim: str = "time", alpha: float = 0.05) -> xr.Dataset:
    """Apply :func:`analyze_series` over the time dimension of an xarray array."""

    if dim not in data.dims:
        raise ValueError(f"DataArray must contain the analysis dimension {dim!r}")

    outputs = xr.apply_ufunc(
        _analyze_tuple,
        data,
        input_core_dims=[[dim]],
        output_core_dims=[[], [], [], [], [], []],
        vectorize=True,
        dask="parallelized",
        output_dtypes=[float, float, bool, float, float, int],
        kwargs={"alpha": alpha},
    )
    names = ["slope", "p_value", "significant", "ci_low", "ci_high", "n_obs"]
    return xr.Dataset(dict(zip(names, outputs, strict=True)))


def load_time_series(source: str | Path | xr.DataArray | xr.Dataset, variable: str | None = None) -> xr.DataArray:
    """Load a 1D or gridded time series from xarray-compatible input."""

    if isinstance(source, xr.DataArray):
        return source
    if isinstance(source, xr.Dataset):
        dataset = source
    else:
        dataset = xr.open_dataset(source)
    if variable is None:
        if len(dataset.data_vars) != 1:
            raise ValueError("Specify variable when the dataset contains multiple data variables")
        variable = next(iter(dataset.data_vars))
    return dataset[variable]


def changepoint_detection_skeleton(values: Any, min_segment_length: int = 5) -> list[int]:
    """Placeholder for a future changepoint detector.

    The interface is intentionally stable while the team evaluates PELT,
    binary segmentation, and climate-specific approaches after the challenge
    release. It currently returns no candidates rather than claiming a method.
    """

    del values, min_segment_length
    return []
