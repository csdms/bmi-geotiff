import pkg_resources

from .bmi import BmiGeoTiff
from .io import GeoTiff

__all__ = ["GeoTiff", "BmiGeoTiff"]
__version__ = pkg_resources.get_distribution("bmi_geotiff").version
