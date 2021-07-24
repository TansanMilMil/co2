#!/bin/bash

/usr/bin/python3 /home/pi/co2/co2-observer/start.py &
/usr/bin/node /home/pi/co2/co2-api/app.js &
/usr/bin/chromium-browser /home/pi/co2/co2-display/index.html --kiosk
