"""Test the bmi_geotiff.io module"""
from pathlib import Path

import pytest
from rasterio.errors import RasterioIOError
from xarray import DataArray

from bmi_geotiff import GeoTiff

TEST_FILE = "RGB.byte.tif"


def test_instantiate_without_filename():
    g = GeoTiff()
    assert isinstance(g, GeoTiff)
    assert g.filename is None
    assert g.da is None


def test_bad_filename(tmpdir, shared_datadir):
    with pytest.raises(RasterioIOError):
        GeoTiff("foo.tif")


def test_with_filename(shared_datadir):
    f = Path(shared_datadir) / TEST_FILE
    g = GeoTiff(f)
    assert isinstance(g, GeoTiff)
    assert g.filename == f
    assert isinstance(g.da, DataArray)


def test_with_filename_as_keyword(shared_datadir):
    f = Path(shared_datadir) / TEST_FILE
    g = GeoTiff(filename=f)
    assert isinstance(g, GeoTiff)
    assert g.filename == f
    assert isinstance(g.da, DataArray)


def test_open(shared_datadir):
    g = GeoTiff()
    f = Path(shared_datadir) / TEST_FILE
    g.open(f)
    assert g.filename == f
    assert isinstance(g.da, DataArray)
