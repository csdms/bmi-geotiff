"""An example of using the GeoTiff data component.

The example is adapted from http://xarray.pydata.org/en/stable/examples/visualization_gallery.html#imshow()-and-rasterio-map-projections,
and it uses the sample GeoTIFF image "RGB.byte.tif" from the rasterio project.
"""
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from bmi_geotiff import GeoTiff

tif_file = "RGB.byte.tif"

g = GeoTiff(tif_file)
print(g.da)

crs = ccrs.UTM("18N")
ax = plt.subplot(projection=crs)
g.da.plot.imshow(ax=ax, rgb="band", transform=crs)
plt.show()
