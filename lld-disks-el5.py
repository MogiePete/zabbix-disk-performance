#!/usr/bin/python
import os
import simplejson as json

# Define any() function since not defined in python 2.4
try:
    any
except NameError:
    def any(s):
        for v in s:
            if v:
                return True
        return False

if __name__ == "__main__":
    # Iterate over all block devices, but ignore them if they are in the
    # skippable set
    skippable = ("sr", "loop", "ram")
    #Changed from /sys/class/block to /sys/block to support EL5
    devices = (device for device in os.listdir("/sys/block")
               if not any(ignore in device for ignore in skippable))
    data = [{"{#DEVICENAME}": device} for device in devices]
    print(json.dumps({"data": data}, indent=4))
