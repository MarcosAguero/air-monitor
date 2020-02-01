#enconding: utf-8
from Adafruit_IO import Client
import AirMonitor as air
from sense_hat import SenseHat
import Screen as screen
import EnvironmentChecker as envCh
import time

# Adafruit_IO
ADAFRUIT_IO_USERNAME = ""
ADAFRUIT_IO_KEY = ""

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
airMonitor = air.AirMonitor('/dev/ttyUSB0')  # port

# Sense Hat
sense = SenseHat()
screen = screen.Screen(sense)


def uploadData_to_adafruit_io(pmtwofive, pmten):
    aio.send('air-monitor-pm-two-five', pmtwofive)
    aio.send('air-monitor-pm-ten', pmten)
    aio.send('air-monitor-humidity', humidityValue)
    print("Envio pmtwofive: " + str(pmtwofive) + " pmten: " + str(pmten))


def start_air_read_save():
    # Set read loop timer
    time_to_read_again = 10  # seconds to wait
    monitor_timer = time.time()

    while True:
        humidityValue = environmentChecker.get_humidity_round_by(1)

        if humidityValue < 20 or humidityValue > 70:
            break

        currentTime = time.time()
        # Check if passed 1 second
        if currentTime - monitor_timer >= time_to_read_again:
            # Read air monitor
            pmtwofive, pmten = airMonitor.read()
            print(humidityValue)
            print("pmtwofive: " + str(pmtwofive) + " pmten: " + str(pmten))
            #screen.displayMessage("", [0,0,0], [0,0,0] )
            uploadData_to_adafruit_io(pmtwofive, pmten)
            monitor_timer = time.time()


# Humidity bg colors
humidityIsHigh = [255, 0, 0]  # red
humidityIsOk = [0, 255, 0]  # green
humidityIsLow = [0, 0, 255]  # blue

environmentChecker = envCh.EnvironmentChecker(sense)

# Check Humidity to begin to sense air
humidityValue = environmentChecker.get_humidity_round_by(1)
print("Humedad Inicial= " + str(humidityValue))

if humidityValue <= 20:
    bgColor = humidityIsLow

elif humidityValue > 20 and humidityValue < 70:
    bgColor = humidityIsOk
    start_air_read_save()

else:
    bgColor = humidityIsHigh

print("bgColor= " + str(bgColor))
