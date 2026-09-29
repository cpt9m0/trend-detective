"""Map visualization skeleton for gridded trend outputs."""

from __future__ import annotations

import matplotlib.pyplot as plt
import xarray as xr


def make_map_skeleton(
    field: xr.DataArray,
    *,
    title: str = "Spatial trend map (skeleton)",
) -> plt.Figure:
    """Render a simple latitude/longitude heatmap for a gridded field."""

    figure, axis = plt.subplots(figsize=(9, 4.5), constrained_layout=True)
    field.plot(ax=axis, cmap="RdBu_r", center=0, add_colorbar=True)
    axis.set_title(title)
    axis.set_xlabel("Longitude")
    axis.set_ylabel("Latitude")
    return figure
