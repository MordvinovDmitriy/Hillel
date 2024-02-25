#!/usr/bin/python3

byte_str = b'r\xc3\xa9sum\xc3\xa9'
byte_dec = byte_str.decode()
print(byte_dec)
byte_lat = byte_dec.encode('latin1')
print(byte_lat)
lat_enc = byte_lat.decode('latin1')
print(lat_enc)
