#!/usr/bin/env python

import sys
import pynmea2
from geojson import MultiPoint

# pynmea: https://github.com/Knio/pynmea2
# geojson: https://github.com/frewsxcv/python-geojson


def lonlat(nmea):
    msg = pynmea2.parse(nmea)
    return (msg.longitude, msg.latitude)


def nmea_file_to_points(filename):
    with open('test.nmea') as f:
        points = MultiPoint([ lonlat(line) for line in f ])
    return points


if __name__=='__main__':
    if (len(sys.argv) < 2):
        print("Usage: %s <input-file>" % __file__)
        sys.exit()
    print(nmea_file_to_points(sys.argv[1]))
