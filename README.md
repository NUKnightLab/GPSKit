# GPSKit
A collection of useful things we have learned about working with GPS hardware and data

## Resources
http://freenmea.net

## Tools

`test.nmea` is just a random sample generated by the freenmea.net emitter: http://freenmea.net/emitter
`nmea2geojson.py` Converts a file of NMEA strings to a GeoJSON multipoint

## Feather GPSKit

This kit is based on the Adafruit Feather system using the Adalogger and the Ultimate GPS Feather wing. Other kits may follow at some point

The full set of materials is in this wishlist: https://www.adafruit.com/wishlists/446492. Notes:
  - the antenna and adapter are optional
  - coin cell is only really needed for the GPS
  - select a 3.7v LiPoly battery according to your mAh (capacity) and weight requirements
  - choose either the 32u4 or the M0 Adalogger. At the moment we are anticipating that either will work

### Assembly

 - solder short female stacking headers onto your Adalogger
 - solder standard male headers onto your GPS wing
 - stack them together

### Code

TBD

[KnightLab_GPS](https://github.com/NUKnightLab/KnightLab_GPS) has GPS reading code

[SensorGrid](https://github.com/NUKnightLab/SensorGrid) has SD card [logging code](https://github.com/NUKnightLab/SensorGrid/blob/master/io.cpp#L139)

## Data Wrangling and hosting

TBD. Will probably do a reference example using S3 to host the data. Perhaps GitHub static files also

## Mapping

TBD
