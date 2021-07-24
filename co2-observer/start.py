import os
import index
import time

os.environ['MYSQL_HOST'] = 'localhost'
os.environ['MYSQL_DATABASE'] = 'co2_observer'
os.environ['MYSQL_USER'] = 'app'
os.environ['MYSQL_PASSWORD'] = 'raspberrypi3'

while True:
    index.get_co2()
    time.sleep(10)
        
