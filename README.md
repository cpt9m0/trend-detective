# Trend Detective

Starter repository for **The Selection Lab** at the 2026 NASA International Space Apps Challenge.

## Challenge

**Be An Earth System Trend Detective!** (Advanced; Earth Science + Software)

The intended solution should examine variables measured by NASA missions or produced by NASA models, visualize how they change over time, and determine:

- **What** is changing
- **Where** it is changing
- **How much** it is changing
- Whether the change is statistically significant

The event is listed in our project brief as **November 14–15, 2026, Austin, Texas**. Full challenge details and official data resources are still pending; this repository deliberately avoids committing to one variable, method, or finished demo.

## Team

- `cpt9m0`
- `Tatiana`

## Current status

This is reusable scaffolding and verified data reconnaissance, not a final hackathon solution. The demo runs on synthetic data and does not require NASA credentials.

## Quick start

```bash
uv sync
uv run pytest -q
uv run ruff check .
uv run streamlit run app/app.py
```

Optional package entry point:

```bash
uv run trend-detective
```

Earthdata access is intentionally lazy. Configure `earthaccess` through its supported login flow only when working with real data; never commit tokens or downloaded raw files.

## Repository layout

```text
app/                         Streamlit demo skeleton
src/trend_detective/
  analysis/                  Mann-Kendall, Theil-Sen, regression, xarray API
  data/                      verified catalog and earthaccess connector
  viz/                       Plotly time series and matplotlib map skeleton
data/raw/                    local raw downloads; ignored by git
data/processed/              local derived data; ignored by git
docs/                        catalog, strategy, and challenge notes
notebooks/                   exploration notebooks
tests/                       analysis, catalog, and visualization tests
```

## Verified candidate data sources

The complete catalog is in [`docs/data_catalog.md`](docs/data_catalog.md). Each row has an Earthdata collection identifier, access record, source agency/DAAC, variable, resolution, and rationale. The current shortlist contains eight records verified against NASA's Common Metadata Repository on **September 29, 2026**.

| Candidate | Variable | NASA access record |
|---|---|---|
| MOD13Q1 V061 | NDVI/EVI | [Earthdata record](https://search.earthdata.nasa.gov/search/granules?p=C1748066515-LPCLOUD) |
| MOD11A2 V061 | Land surface temperature | [Earthdata record](https://search.earthdata.nasa.gov/search/granules?p=C2269056084-LPCLOUD) |
| GPM IMERG Final V07 | Precipitation | [Earthdata record](https://search.earthdata.nasa.gov/search/granules?p=C2723754864-GES_DISC) |
| MUR SST v4.1 | Sea surface temperature | [Earthdata record](https://search.earthdata.nasa.gov/search/granules?p=C1996881146-POCLOUD) |
| SMAP SPL3SMP_E V005 | Soil moisture | [Earthdata record](https://search.earthdata.nasa.gov/search/granules?p=C2872801341-NSIDC_CPRD) |
| NSIDC-0079 V004 | Sea ice concentration | [Earthdata record](https://search.earthdata.nasa.gov/search/granules?p=C3177837864-NSIDC_CPRD) |
| GRACE/GRACE-FO JPL Mascon RL06.3 V04 | Equivalent water height | [Earthdata record](https://search.earthdata.nasa.gov/search/granules?p=C3195502222-POCLOUD) |
| GRACE-DA-DM Global V3.0 | Drought indicators | [Earthdata record](https://search.earthdata.nasa.gov/search/granules?p=C2283200566-GES_DISC) |

## Methodology plan

1. Select a candidate variable and document its provenance, license, units, quality flags, and temporal/spatial coverage.
2. Use `earthaccess` for authenticated search/open operations; keep connectors separate from analysis so synthetic tests remain deterministic.
3. Normalize time coordinates, missing values, units, and quality masks before analysis.
4. Run a robust Theil-Sen slope and Mann-Kendall significance test; retain p-value, alpha, confidence interval, and valid-observation count.
5. Compare with ordinary least-squares slope and p-value as a diagnostic, not as the only result.
6. Aggregate or map gridded outputs to answer what/where/how much; preserve the original resolution in metadata.
7. Add changepoint detection only after the challenge's intended question and evaluation criteria are known.
8. Report limitations, multiple-testing considerations, temporal autocorrelation, data gaps, and any known product artifacts.

## License and data rights

Original repository content defaults to Apache 2.0. Third-party datasets remain subject to their own terms and citations. Before publishing a final submission, the team must verify that every code, image, font, notebook, and data artifact is openly licensed and that the repository can warrant publication rights.

See [`LICENSE`](LICENSE) and [`docs/data_catalog.md`](docs/data_catalog.md) for the current provenance record.

## Pending full challenge release

The official full challenge statement, evaluation details, required datasets, and any event-specific constraints were not available in the project brief used to scaffold this repository. Do not treat the current shortlist or synthetic demo as the final solution direction.
