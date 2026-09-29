from trend_detective.data.catalog import DATASETS, get_dataset


def test_catalog_has_verified_candidate_collections():
    assert 6 <= len(DATASETS) <= 10
    assert all(dataset.status == "verified" for dataset in DATASETS)
    assert all(dataset.collection_id and dataset.earthdata_url for dataset in DATASETS)


def test_catalog_lookup_is_stable():
    assert get_dataset("gpm_imerg_daily").variable == "Daily mean precipitation"
