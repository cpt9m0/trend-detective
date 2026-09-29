"""Plotly time-series visualization helpers."""

from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import xarray as xr

from trend_detective.analysis.trends import TrendResult


def make_timeseries_figure(
    series: xr.DataArray,
    result: TrendResult,
    title: str | None = None,
) -> go.Figure:
    """Create a time-series chart with robust trend line and significance note."""

    x = series[series.dims[0]].values if series.ndim else np.arange(series.size)
    y = series.values
    valid = np.isfinite(y)
    x_valid = np.asarray(x)[valid]
    order = np.arange(len(y), dtype=float)[valid]
    if order.size:
        trend = y[valid][0] + result.slope * (order - order[0])
    else:
        trend = np.array([])

    figure = go.Figure()
    figure.add_trace(go.Scatter(x=x_valid, y=y[valid], mode="lines+markers", name="Observed"))
    figure.add_trace(go.Scatter(x=x_valid, y=trend, mode="lines", name="Theil-Sen trend"))
    significance = "statistically significant" if result.significant else "not statistically significant"
    figure.update_layout(
        title=title or "Earth system variable trend",
        xaxis_title="Time",
        yaxis_title=series.name or "Value",
        annotations=[
            {
                "text": f"Slope: {result.slope:.4g} per observation; p={result.p_value:.3g} ({significance})",
                "xref": "paper",
                "yref": "paper",
                "x": 0,
                "y": 1.12,
                "showarrow": False,
            }
        ],
        template="plotly_white",
    )
    return figure
