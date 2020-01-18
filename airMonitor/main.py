from Adafruit_IO import Client
import AirMonitor
from sense_hat import SenseHat
import Screen
import EnvironmentChecker
import monitor
import time

# Adafruit_IO
ADAFRUIT_IO_USERNAME = ""
ADAFRUIT_IO_KEY = ""

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
airMonitor = AirMonitor()
airMonitor.sensorPath('/dev/tty.usbserial-1420')

screen = Screen()


def uploadData_to_adafruit_io(pmtwofive, pmten):
    aio.send('air-monitor-pm-two-five', pmtwofive)
    aio.send('air-monitor-pm-ten', pmten)


def start_air_read_save():
    # Set read loop timer
    time_to_read_again = 1  # seconds to wait
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
            uploadData_to_adafruit_io(pmtwofive, pmten)
            monitor_timer = time.time()


# Humidity bg colors
humidityIsHigh = (255, 0, 0)  # red
humidityIsOk = (0, 255, 0)  # green
humidityIsLow = (0, 0, 255)  # blue

environmentChecker = EnvironmentChecker()
# Check Humidity to begin to sense air
humidityValue = environmentChecker.get_humidity_round_by(1)
print("Humedad Inicial= " . humidityValue)

if humidityValue <= 20:
    bgColor = humidityIsLow

elif humidityValue > 20 and humidityValue < 70:
    bgColor = humidityIsOk
    start_air_read_save()

else:
    bgColor = humidityIsHigh

print("bgColor= " . bgColor)
