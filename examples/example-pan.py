"""An example of using the GeoTiff data component.

The data used are band 1 of Landsat 7 ETM scene LE71030642021102ASA00.
"""
import matplotlib.pyplot as plt

from bmi_geotiff import GeoTiff

url = "https://csdms.colorado.edu/data/LE07_L1GT_103064_20210412_20210412_02_RT_B1.TIF"

g = GeoTiff()
g.open(url)
print(g.da)

band = g.da.squeeze("band")
print(band)

band.plot.imshow()
plt.show()
