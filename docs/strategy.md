# Strategy after the full challenge release

## Reusable now

- NASA Earthdata connector boundary using `earthaccess`; authentication remains outside source control.
- Collection catalog with provenance fields and stable keys.
- xarray loading for 1D and gridded time series.
- Missing-value handling, Theil-Sen slope, Mann-Kendall p-value, confidence interval, and ordinary least-squares diagnostic.
- Plotly time-series chart and matplotlib gridded-map skeleton.
- Streamlit synthetic-data demo and pytest coverage.
- Raw-data and credential hygiene.

## Deliberately open

- The selected Earth system variable and geographic case study.
- Quality flags, masking, resampling, unit conversions, and temporal aggregation for the final product.
- Spatial multiple-testing correction and treatment of temporal autocorrelation.
- Changement-point method and thresholds.
- Final story, UI, deployment target, and challenge-specific evaluation hooks.

## Hackathon day 1 checklist

- [ ] Read the complete official challenge statement and evaluation rubric.
- [ ] Confirm required NASA mission/model data and permitted access routes.
- [ ] Pick one question that can answer what/where/how much/significance in the available time.
- [ ] Record dataset version, license/terms, citation, units, QA fields, and access date.
- [ ] Download a small reproducible subset and commit only metadata/configuration.
- [ ] Establish a baseline plot before adding advanced statistics.
- [ ] Add tests for the selected variable's missing-value and unit behavior.
- [ ] Decide whether the spatial result needs false-discovery control or block-bootstrap uncertainty.
- [ ] Capture a short limitations statement before polishing the UI.
- [ ] Recheck every original and third-party asset against the publication-rights warrant.
