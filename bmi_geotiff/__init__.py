import pkg_resources

from .io import GeoTiff
from .bmi import BmiGeoTiff

__all__ = ["GeoTiff", "BmiGeoTiff"]
__version__ = pkg_resources.get_distribution("bmi_geotiff").version
