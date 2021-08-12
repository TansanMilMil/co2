import os
import index
import time

os.environ['MYSQL_HOST'] = 'localhost'
os.environ['MYSQL_DATABASE'] = 'co2_observe'
os.environ['MYSQL_USER'] = 'raspberrypi'
os.environ['MYSQL_PASSWORD'] = 'raspberrypi'

while True:
    index.get_co2()
    time.sleep(10)
        
