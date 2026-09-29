# Candidate NASA datasets

**Verification date:** September 29, 2026. **Verification method:** exact collection lookup in NASA's Common Metadata Repository (CMR), followed by checking the linked Earthdata/DAAC record. A row is marked **verified** only when the collection identifier, title, and access record resolve. The official challenge may later require a different product or license review.

| Key | Variable | Mission/model source | Spatial / temporal resolution | Access path and citation | Why it fits |
|---|---|---|---|---|---|
| `modis_ndvi_250m` | NDVI, EVI | Terra MODIS; LP DAAC | 250 m; 16-day global composites; record begins 2000-02-18 | [CMR collection C1748066515-LPCLOUD](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=MOD13Q1&version=061); [Earthdata granules](https://search.earthdata.nasa.gov/search/granules?p=C1748066515-LPCLOUD) | Long vegetation-index record with quality layers and spatial detail for land-cover/vegetation trends. |
| `modis_lst_1km` | Day/night land-surface temperature and emissivity | Terra MODIS; LP DAAC | 1 km; 8-day global composites; record begins 2000-02-18 | [CMR collection C2269056084-LPCLOUD](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=MOD11A2&version=061); [Earthdata granules](https://search.earthdata.nasa.gov/search/granules?p=C2269056084-LPCLOUD) | Regular global composites support heat-trend analysis while retaining spatial structure. |
| `gpm_imerg_daily` | Daily mean precipitation | NASA/JAXA GPM; GES DISC | 0.1° grid; daily final product derived from half-hourly observations | [CMR collection C2723754864-GES_DISC](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=GPM_3IMERGDF&version=07); [Earthdata granules](https://search.earthdata.nasa.gov/search/granules?p=C2723754864-GES_DISC) | Enables drought, flood, and hydroclimate trend questions; product metadata explicitly describes latency and quality limitations. |
| `mur_sst` | Sea-surface temperature and anomaly | NASA MEaSUREs/JPL PO.DAAC; multi-sensor GHRSST analysis | 0.01° global grid; hourly-to-less-than-daily granule cadence; starts 2002-05-31 | [PO.DAAC collection](https://podaac.jpl.nasa.gov/dataset/MUR-JPL-L4-GLOB-v4.1); [CMR collection C1996881146-POCLOUD](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=MUR-JPL-L4-GLOB-v4.1&version=4.1) | High-resolution SST and anomaly fields support ocean-warming and regional anomaly maps. |
| `smap_soil_moisture` | Surface soil moisture | NASA SMAP; NSIDC DAAC | 9 km EASE-Grid; daily global and polar composites; starts 2015-03-31 | [CMR collection C2872801341-NSIDC_CPRD](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=SPL3SMP_E&version=005); [NSIDC user guide](https://nsidc.org/sites/default/files/spl3smp_e-v005-userguide.pdf) | Direct land-surface moisture signal for drought and agriculture-related trends. |
| `bootstrap_sea_ice` | Sea-ice concentration | Nimbus-7 SMMR and DMSP SSM/I-SSMIS passive microwave; NSIDC DAAC | 25 km polar stereographic grids; daily and monthly; 1978-11-01 through 2025-12-31 in the verified page | [NSIDC-0079 Version 4](https://nsidc.org/data/nsidc-0079/versions/4); [CMR collection C3177837864-NSIDC_CPRD](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=NSIDC-0079&keyword=Bootstrap) | Long polar record supports sea-ice decline and regional seasonality detection. |
| `grace_mascons` | Equivalent water-height anomaly | NASA GRACE/GRACE-FO; JPL Mascon solution; PO.DAAC | Monthly global equal-area 3° mascon grid; starts 2002-04-04 | [GRACE/JPL data page](https://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/); [CMR collection C3195502222-POCLOUD](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=TELLUS_GRAC-GRFO_MASCON_GRID_RL06.3_V4&version=RL06.3Mv04) | Monthly water-storage anomalies support basin hydrology, ice-mass, and ocean-mass trend studies. |
| `grace_drought_indicators` | Groundwater, root-zone, and surface-soil-moisture percentiles | NASA GRACE/GRACE-FO data assimilation with Catchment Land Surface Model; GES DISC | 0.25° global grid; weekly indicators; starts 2003-02-03 | [CMR collection C2283200566-GES_DISC](https://cmr.earthdata.nasa.gov/search/collections.json?short_name=GRACEDADM_CLSM025GL_7D&version=3.0); [GES DISC documentation](https://docserver.gesdisc.eosdis.nasa.gov/public/project/hydrology/README_GRACEDADM3GL.pdf) | Demonstrates trend detection on NASA-produced model outputs as well as observations. |

## Rights and citation checklist

- Confirm the current dataset citation and terms at the DAAC page immediately before publication.
- Preserve the collection ID, version, subset, access date, and any DOI in the final report.
- Download only the smallest reproducible subset needed for analysis.
- Keep raw data outside git; the repository ignores local raw and processed data directories.
- Do not assume an open data license makes third-party documentation, imagery, or derived assets automatically publishable.

## Unverified / intentionally open

- No candidate is yet the selected challenge variable.
- No license warranty has been issued for a final submission bundle.
- No official 2026 challenge-specific dataset requirement has been inferred from this shortlist.
