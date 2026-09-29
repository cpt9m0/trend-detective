import numpy as np
import pandas as pd
import streamlit as st
import xarray as xr

from trend_detective.analysis.trends import analyze_series
from trend_detective.data.catalog import DATASETS
from trend_detective.viz.timeseries import make_timeseries_figure

st.set_page_config(page_title="Trend Detective", layout="wide")
st.title("Be An Earth System Trend Detective")
st.caption("Reusable scaffold; synthetic data only until the official 2026 challenge details are released.")

with st.sidebar:
    st.header("Candidate dataset")
    selected_key = st.selectbox("Dataset", [dataset.key for dataset in DATASETS])
    selected = next(dataset for dataset in DATASETS if dataset.key == selected_key)
    st.write(f"**Variable:** {selected.variable}")
    st.write(f"**Source:** {selected.source}")
    st.write(f"**Resolution:** {selected.resolution}")
    st.link_button("Open Earthdata record", selected.earthdata_url)

st.info("The selectors are wired to the verified catalog, but the demo uses a synthetic series so no data or credentials are downloaded.")

periods = st.slider("Synthetic observations", min_value=12, max_value=120, value=48, step=12)
noise = st.slider("Synthetic noise", min_value=0.0, max_value=2.0, value=0.35, step=0.05)
seed = st.number_input("Random seed", min_value=0, max_value=9999, value=7, step=1)

rng = np.random.default_rng(seed)
times = pd.date_range("2000-01-01", periods=periods, freq="MS")
values = 0.08 * np.arange(periods) + rng.normal(0, noise, periods)
series = xr.DataArray(values, dims="time", coords={"time": times}, name=selected.variable)
result = analyze_series(series.values, times=times)

left, right = st.columns([2, 1])
with left:
    st.plotly_chart(make_timeseries_figure(series, result, title=selected.title), use_container_width=True)
with right:
    st.subheader("Significance report")
    st.metric("Theil-Sen slope", f"{result.slope:.4f} / observation")
    st.metric("Mann-Kendall p-value", f"{result.p_value:.4g}")
    st.metric("Valid observations", result.n_obs)
    st.success("Significant at α=0.05" if result.significant else "Not significant at α=0.05")
    st.write({"95% CI": result.confidence_interval, "changepoints": "not enabled yet"})

st.divider()
st.subheader("Next integration point")
st.code("EarthdataConnector().authenticate(); EarthdataConnector().search(...)\nload_time_series(...); analyze_dataarray(...)")
st.caption("Never commit Earthdata credentials or large raw downloads. Keep source citations with every selected collection.")
