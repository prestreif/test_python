#!/usr/bin/env python3.6

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []

for val in mac:
    #print(key.replace(":", "."))
    mac_cisco.append(val.replace(":", "."))

print(mac_cisco)
