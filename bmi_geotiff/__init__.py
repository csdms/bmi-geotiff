import pkg_resources

from .io import GeoTiff

__all__ = ["GeoTiff"]
__version__ = pkg_resources.get_distribution("bmi_geotiff").version
