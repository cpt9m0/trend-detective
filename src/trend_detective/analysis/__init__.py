"""Trend Detective analysis package."""

from .trends import (
    TrendResult,
    analyze_dataarray,
    analyze_series,
    changepoint_detection_skeleton,
    linear_regression,
    mann_kendall_test,
    theil_sen_slope,
)

__all__ = [
    "TrendResult",
    "analyze_dataarray",
    "analyze_series",
    "changepoint_detection_skeleton",
    "linear_regression",
    "mann_kendall_test",
    "theil_sen_slope",
]
