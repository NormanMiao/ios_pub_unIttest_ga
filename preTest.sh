#!/bin/bash
pkill -f "goios --udid $UDT_DEVICE_SERIAL forward"
goios --udid $UDT_DEVICE_SERIAL forward $GA_SDK_PORT 27029 &
#adb forward tcp:$GA_SDK_PORT tcp:27029
echo "forward end"
