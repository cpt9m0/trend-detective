import numpy as np
import pandas as pd
import xarray as xr

from trend_detective.analysis.trends import analyze_series
from trend_detective.viz.timeseries import make_timeseries_figure


def test_timeseries_figure_contains_observed_and_trend_traces():
    series = xr.DataArray(
        np.arange(6, dtype=float),
        dims="time",
        coords={"time": pd.date_range("2024-01-01", periods=6)},
        name="synthetic",
    )
    figure = make_timeseries_figure(series, analyze_series(series.values))

    assert len(figure.data) == 2
    assert {trace.name for trace in figure.data} == {"Observed", "Theil-Sen trend"}
    assert "p=" in figure.layout.annotations[0].text
