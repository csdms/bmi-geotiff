[![Basic Model Interface](https://img.shields.io/badge/CSDMS-Basic%20Model%20Interface-green.svg)](https://bmi.readthedocs.io/)
[![PyPI](https://img.shields.io/pypi/v/bmi-geotiff)](https://pypi.org/project/bmi-geotiff)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/bmi-geotiff.svg)](https://anaconda.org/conda-forge/bmi-geotiff)
[![Build/Test CI](https://github.com/csdms/bmi-geotiff/actions/workflows/build-test-ci.yml/badge.svg)](https://github.com/csdms/bmi-geotiff/actions/workflows/build-test-ci.yml)
[![Documentation Status](https://readthedocs.org/projects/bmi-geotiff/badge/?version=latest)](https://bmi-geotiff.readthedocs.io/en/latest/?badge=latest)

# bmi-geotiff

Access data (and metadata) from a GeoTIFF file through an API or a BMI.

The *bmi-geotiff* library accepts a filepath or an URL to a GeoTIFF file.
Data are loaded into an
[xarray](http://xarray.pydata.org/en/stable/)
[DataArray](http://xarray.pydata.org/en/stable/api.html#dataarray)
using the experimental [open_rasterio](http://xarray.pydata.org/en/stable/generated/xarray.open_rasterio.html#xarray.open_rasterio) method.
The API is wrapped with a
[Basic Model Interface](https://bmi.readthedocs.io) (BMI),
which provides a standard set of functions for coupling with data or models
that also expose a BMI.
More information on the BMI can found in its
[documentation](https://bmi.readthedocs.io).

## Installation

Install the latest stable release of *bmi-geotiff* with `pip`:
```
pip install bmi-geotiff
```
or with `conda`:
```
conda install -c conda-forge bmi-geotiff
```

Alternately,
the *bmi-geotiff* library can be built and installed from source.
The library uses several other open source libraries,
so a convenient way of building and installing it is within a
[conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).
After cloning or downloading the *bmi-geotiff*
[repository](https://github.com/csdms/bmi-geotiff),
change into the repository directory
and set up a conda environment with the included environment file:
```
conda env create --file=environment.yml
```
Then build and install *bmi-geotiff* from source with
```
make install
```

## Examples

A brief example of using the *bmi-geotiff* API is given in the following steps.
The example is derived from a [similar example](http://xarray.pydata.org/en/stable/examples/visualization_gallery.html#imshow()-and-rasterio-map-projections) in the xarray documentation.

Start a Python session and import the `GeoTiff` class:
```python
>>> from bmi_geotiff import GeoTiff
```

For convenience,
let's use a test image from the [rasterio](https://rasterio.readthedocs.io) project: 
```python
>>> url = "https://github.com/mapbox/rasterio/raw/master/tests/data/RGB.byte.tif"
```

Make an instance of `GeoTiff` with this URL:
```python
>>> g = GeoTiff(url)
```
This step might take a few moments as the data are pulled from GitHub.

The data have been loaded into an xarray `DataArray`, which can be accessed through the `da` property:
```python
>>> print(g.da)
<xarray.DataArray (band: 3, y: 718, x: 791)>
[1703814 values with dtype=uint8]
Coordinates:
  * band     (band) int64 1 2 3
  * y        (y) float64 2.827e+06 2.826e+06 2.826e+06 ... 2.612e+06 2.612e+06
  * x        (x) float64 1.021e+05 1.024e+05 1.027e+05 ... 3.389e+05 3.392e+05
Attributes:
    transform:      (300.0379266750948, 0.0, 101985.0, 0.0, -300.041782729805...
    crs:            +init=epsg:32618
    res:            (300.0379266750948, 300.041782729805)
    is_tiled:       0
    nodatavals:     (0.0, 0.0, 0.0)
    scales:         (1.0, 1.0, 1.0)
    offsets:        (0.0, 0.0, 0.0)
    AREA_OR_POINT:  Area
```

Display the image with the [xarray.plot.imshow](http://xarray.pydata.org/en/stable/generated/xarray.plot.imshow.html) method.
```python
>>> import matplotlib.pyplot as plt
>>> g.da.plot.imshow()
>>> plt.show()
```

![Example GeoTiff display through *xarray*.](./examples/example-rgb.png)

For examples with more detail,
see the Jupyter Notebooks and Python scripts
included in the [examples](https://github.com/csdms/bmi-geotiff/tree/main/examples) directory
of the *bmi-geotiff* repository.

Documentation for *bmi-geotiff*
is available at https://bmi-geotiff.readthedocs.io.
