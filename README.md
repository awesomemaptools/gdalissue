# Issue with gdal.Open()

Some files (possibly corrupt) will only return a valid dataset if there's an *.aux.xml file by the same name.

Test gdal.Open with the python script here:
```
./gdalOpen.py tmpfile1.tif
# Nice output ...

# Rename tmpfile1.tif.aux.xml to _tmpfile1.tif.aux.xml
# Try again:
./gdalOpen.py tmpfile1.tif
# Error output ...
$ ./gdalOpen.py tmpfile1.tif
filename: tmpfile1.tif
ERROR 1: _TIFFVSetField:tmpfile1.tif: Null count for "GeoDoubleParams" (type 12, writecount -1, passcount 1)
<type 'NoneType'>
Traceback (most recent call last):
  File "./gdalOpen.py", line 16, in <module>
    band = ds.GetRasterBand(1)
AttributeError: 'NoneType' object has no attribute 'GetRasterBand'
```
The files tmpfile1 and tmpfile2 are from this WMS service:
http://services.sentinel-hub.com/v1/wms/4f3d9ca1-d534-44d4-9dd2-066243bc7b1a?REQUEST=GetMap&layers=VEGETATION_INDEX___NDVI&styles=INDEX&bbox=-121.951547,36.575766,-121.908631,36.6054&height=120&width=380&CRS=CRS:84&format=image/tiff;depth=32f

Try another file:
```
./gdalOpen.py tmpfile2.tif
# Error output ...

# Rename _tmpfile2.tif.aux.xml to tmpfile2.tif.aux.xml
# Try again:
./gdalOpen.py tmpfile2.tif
# Nice output ...
```

Here's a file from http://download.osgeo.org/geotiff/samples/usgs/
```
./gdalOpen.py m30dem.tif
# Nice output ...

```

Get more sample files here:
http://download.osgeo.org/geotiff/samples/
