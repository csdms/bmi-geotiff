"""Access GeoTIFF files."""
import rioxarray


class GeoTiff:

    """Access data and metadata in a GeoTIFF file."""

    def __init__(self, filename=None):
        """Make a GeoTiff object.

        Parameters
        ----------
        filename : str, optional
            Path or URL to the file to open.
        """
        self._filename = None
        self._da = None

        if filename is not None:
            self.open(filename)

    @property
    def filename(self):
        return self._filename

    @property
    def da(self):
        return self._da

    def open(self, filename):
        """Load a GeoTIFF file into an xarray DataArray.

        Parameters
        ----------
        filename : str
            Path or URL to the file to open.
        """
        self._filename = filename
        self._da = rioxarray.open_rasterio(self._filename)
        try:
            band = self._da.squeeze("band")
        except ValueError:
            pass
        else:
            self._da = band
