import serial
import time
from Adafruit_IO import Client
from datetime import datetime


# Adafruit_IO
ADAFRUIT_IO_USERNAME = ""
ADAFRUIT_IO_KEY = ""

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
ser = serial.Serial('/dev/ttyUSB0')
f= open("guru99.txt","w+")

now = datetime.now().time() # time object


while True:
    data = []
    for index in range(0, 10):
        datum = ser.read()
        data.append(datum)
        f=open("guru99.txt", "a+")

    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    print("pmtwofive" + str(pmtwofive) )
    now = datetime.now().time()
    f.write("Time: " + str(now))
    f.write("pmtwofive: %d\r\n" % (pmtwofive))
    aio.send('air-monitor-pm-two-five', pmtwofive)
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    f.write("pmten: %d\r\n" % (pmten))
    print("pmten" + str(pmten) )
    aio.send('air-monitor-pm-ten', pmten)
    f.close() 
    time.sleep(10)
