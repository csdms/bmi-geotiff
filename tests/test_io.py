"""Test the bmi_geotiff.io module"""
from bmi_geotiff import GeoTiff


def test_instantiate():
    g = GeoTiff()
    assert isinstance(g, GeoTiff)
