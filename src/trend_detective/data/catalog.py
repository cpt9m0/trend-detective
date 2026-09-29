"""Verified candidate datasets for the 2026 challenge."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DatasetEntry:
    """A candidate Earth system dataset with provenance metadata."""

    key: str
    title: str
    variable: str
    source: str
    resolution: str
    access_path: str
    collection_id: str
    earthdata_url: str
    why_fit: str
    status: str = "verified"


DATASETS: tuple[DatasetEntry, ...] = (
    DatasetEntry(
        key="modis_ndvi_250m",
        title="MODIS/Terra Vegetation Indices 16-Day L3 Global 250m V061",
        variable="NDVI or EVI",
        source="NASA Terra MODIS; LP DAAC",
        resolution="250 m, 16-day global composites",
        access_path="Earthdata Search / AppEEARS / LP DAAC",
        collection_id="C1748066515-LPCLOUD",
        earthdata_url="https://search.earthdata.nasa.gov/search/granules?p=C1748066515-LPCLOUD",
        why_fit="Long vegetation-index record supports spatial and temporal vegetation trend detection.",
    ),
    DatasetEntry(
        key="modis_lst_1km",
        title="MODIS/Terra Land Surface Temperature/Emissivity 8-Day L3 Global 1km V061",
        variable="Day/night land surface temperature",
        source="NASA Terra MODIS; LP DAAC",
        resolution="1 km, 8-day global composites",
        access_path="Earthdata Search / AppEEARS / LP DAAC",
        collection_id="C2269056084-LPCLOUD",
        earthdata_url="https://search.earthdata.nasa.gov/search/granules?p=C2269056084-LPCLOUD",
        why_fit="Regular global composites enable heat-trend analysis while retaining spatial structure.",
    ),
    DatasetEntry(
        key="gpm_imerg_daily",
        title="GPM IMERG Final Precipitation L3 Daily 0.1 degree V07",
        variable="Daily mean precipitation",
        source="NASA/JAXA GPM; GES DISC",
        resolution="0.1° grid, daily; derived from half-hourly data",
        access_path="Earthdata Search / GES DISC",
        collection_id="C2723754864-GES_DISC",
        earthdata_url="https://search.earthdata.nasa.gov/search/granules?p=C2723754864-GES_DISC",
        why_fit="Daily precipitation supports drought, flood, and hydroclimate trend questions.",
    ),
    DatasetEntry(
        key="mur_sst",
        title="GHRSST Level 4 MUR Global Foundation Sea Surface Temperature v4.1",
        variable="Sea surface temperature and anomaly",
        source="NASA MEaSUREs/JPL PO.DAAC",
        resolution="0.01° global grid; hourly-to-less-than-daily granule cadence",
        access_path="Earthdata Search / PO.DAAC",
        collection_id="C1996881146-POCLOUD",
        earthdata_url="https://search.earthdata.nasa.gov/search/granules?p=C1996881146-POCLOUD",
        why_fit="High-resolution, long-running SST analysis is suited to ocean warming and anomaly maps.",
    ),
    DatasetEntry(
        key="smap_soil_moisture",
        title="SMAP Enhanced L3 Radiometer Global Daily 9 km Soil Moisture V005",
        variable="Surface soil moisture",
        source="NASA SMAP; NSIDC DAAC",
        resolution="9 km EASE-Grid, daily global/polar composites",
        access_path="Earthdata Search / NSIDC DAAC",
        collection_id="C2872801341-NSIDC_CPRD",
        earthdata_url="https://search.earthdata.nasa.gov/search/granules?p=C2872801341-NSIDC_CPRD",
        why_fit="Soil moisture trends connect directly to drought, agriculture, and land-surface change.",
    ),
    DatasetEntry(
        key="bootstrap_sea_ice",
        title="Bootstrap Sea Ice Concentrations from Nimbus-7 SMMR and DMSP SSM/I-SSMIS V004",
        variable="Sea ice concentration",
        source="Nimbus-7/DMSP passive microwave; NSIDC DAAC",
        resolution="25 km polar grids, daily/monthly products",
        access_path="Earthdata Search / NSIDC DAAC",
        collection_id="C3177837864-NSIDC_CPRD",
        earthdata_url="https://search.earthdata.nasa.gov/search/granules?p=C3177837864-NSIDC_CPRD",
        why_fit="A long polar record provides a strong candidate for detecting regional sea-ice decline.",
    ),
    DatasetEntry(
        key="grace_mascons",
        title="JPL GRACE and GRACE-FO Mascon Ocean, Ice, and Hydrology Equivalent Water Height RL06.3 V04",
        variable="Equivalent water-height anomaly",
        source="NASA GRACE/GRACE-FO; JPL PO.DAAC",
        resolution="Monthly global equal-area 3° mascon grid",
        access_path="Earthdata Search / PO.DAAC / GRACE project",
        collection_id="C3195502222-POCLOUD",
        earthdata_url="https://search.earthdata.nasa.gov/search/granules?p=C3195502222-POCLOUD",
        why_fit="Monthly water-storage anomalies support basin-scale hydrology and ice-mass trend studies.",
    ),
    DatasetEntry(
        key="grace_drought_indicators",
        title="GRACE-DA-DM Global Groundwater and Soil Moisture Conditions L4 7-Day V3.0",
        variable="Groundwater, root-zone, and surface-soil-moisture percentiles",
        source="NASA GRACE/GRACE-FO data assimilation with CLSM; GES DISC",
        resolution="0.25° global grid, weekly operational indicators",
        access_path="Earthdata Search / GES DISC",
        collection_id="C2283200566-GES_DISC",
        earthdata_url="https://search.earthdata.nasa.gov/search/granules?p=C2283200566-GES_DISC",
        why_fit="Model-assisted drought indicators demonstrate trend detection on NASA-produced model outputs.",
    ),
)


def get_dataset(key: str) -> DatasetEntry:
    """Return a catalog entry by stable project key."""

    for dataset in DATASETS:
        if dataset.key == key:
            return dataset
    raise KeyError(f"Unknown dataset key: {key}")
