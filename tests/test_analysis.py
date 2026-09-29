import numpy as np
import pandas as pd
import pytest
import xarray as xr

from trend_detective.analysis.trends import (
    TrendResult,
    analyze_dataarray,
    analyze_series,
    changepoint_detection_skeleton,
    linear_regression,
)


def test_analyze_series_detects_known_linear_trend():
    times = pd.date_range("2000-01-01", periods=40, freq="YE")
    values = 2.0 * np.arange(40) + 10.0

    result = analyze_series(values, times=times)

    assert isinstance(result, TrendResult)
    assert result.n_obs == 40
    assert result.slope == pytest.approx(2.0, abs=1e-10)
    assert result.p_value < 0.001
    assert result.significant is True
    assert result.confidence_interval[0] <= 2.0 <= result.confidence_interval[1]


def test_analyze_series_ignores_missing_values():
    values = np.array([1.0, 2.0, np.nan, 4.0, 5.0, np.nan])

    result = analyze_series(values)

    assert result.n_obs == 4
    assert result.slope == pytest.approx(1.0)
    assert result.p_value > 0.0
    assert result.significant is False


def test_analyze_dataarray_returns_spatial_result_for_3d_input():
    data = xr.DataArray(
        np.stack(
            [
                np.arange(8, dtype=float),
                np.arange(8, dtype=float) * -1,
            ],
            axis=1,
        ).reshape(8, 1, 2),
        dims=("time", "lat", "lon"),
        coords={
            "time": pd.date_range("2020-01-01", periods=8),
            "lat": [0],
            "lon": [10, 20],
        },
        name="value",
    )

    result = analyze_dataarray(data)

    assert set(result.data_vars) >= {
        "slope",
        "p_value",
        "significant",
        "ci_low",
        "ci_high",
        "n_obs",
    }
    assert result.slope.sel(lon=10).item() == pytest.approx(1.0)
    assert result.slope.sel(lon=20).item() == pytest.approx(-1.0)


def test_linear_regression_reports_slope_and_p_value():
    result = linear_regression(3.0 * np.arange(20) - 4.0)

    assert result["slope"] == pytest.approx(3.0)
    assert result["p_value"] < 0.001


def test_changepoint_detector_is_explicitly_a_skeleton():
    assert changepoint_detection_skeleton([1, 2, 3, 4]) == []
