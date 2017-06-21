#!/usr/bin/python2

import sys
from osgeo import gdal

# print sys.argv[1:]
try:
  filename = sys.argv[1]
except:
  filename = "tmpfile1.tif"
# filename = "tmpfile1.tif"

print('filename: ' + filename)
ds = gdal.Open(filename)
print(type(ds))
band = ds.GetRasterBand(1)
print(type(band))
data = band.ReadAsArray()
print(type(data), data.shape)
print('value at 1,1:', data[1][1])