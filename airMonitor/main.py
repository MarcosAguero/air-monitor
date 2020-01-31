# enconding: utf-8
from Adafruit_IO import Client
import AirMonitor as air
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import Screen as screen
import EnvironmentChecker as envCh
import time
# shutdown
import Shutdown as shutdown
import os

# Adafruit_IO
ADAFRUIT_IO_USERNAME = ""
ADAFRUIT_IO_KEY = ""

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
airMonitor = air.AirMonitor('/dev/ttyUSB0')  # port

# Sense Hat
sense = SenseHat()
sense.clear()
screen = screen.Screen(sense)

shutdown = shutdown.Shutdown(sense, time, os)
sense.stick.direction_middle = shutdown.pushed_middle  # shutdown
sense.stick.direction_up = shutdown.pushed_up  # cancel


def uploadData_to_adafruit_io(pmtwofive, pmten):
    aio.send('air-monitor-pm-two-five', pmtwofive)
    aio.send('air-monitor-pm-ten', pmten)


def start_air_read_save():
    # Set read loop timer
    time_to_read_again = 10  # seconds to wait
    monitor_timer = time.time()

    while True:
        humidityValue = environmentChecker.get_humidity_round_by(1)

        if humidityValue < 20 or humidityValue > 70:
            screen.displayMessage("", [255, 255, 255], bgColor)
            break

        currentTime = time.time()
        # Check if passed 1 second
        if currentTime - monitor_timer >= time_to_read_again:
            # Read air monitor
            pmtwofive, pmten = airMonitor.read()
            print(humidityValue)
            print("pmtwofive: " + str(pmtwofive) + " pmten: " + str(pmten))
            uploadData_to_adafruit_io(pmtwofive, pmten)

            if pmtwofive < 24:
                txtColor = green
            else:
                txtColor = red

            screen.displayMessage("PM-2.5: " + str(pmtwofive), txtColor, black)

            if pmtwofive < 24:
                txtColor = green
            else:
                txtColor = red

            screen.displayMessage("PM-10: " + str(pmten), txtColor, black)
            monitor_timer = time.time()


# Colors
black = [0, 0, 0]
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
# Humidity bg colors
humidityIsHigh = blue
humidityIsOk = green
humidityIsLow = [0, 232, 255]  # light blue

environmentChecker = envCh.EnvironmentChecker(sense)

# Check Humidity to begin to sense air
humidityValue = environmentChecker.get_humidity_round_by(1)
print("Humedad Inicial= " + str(humidityValue))

if humidityValue <= 20:
    bgColor = humidityIsLow
    screen.displayMessage("low", black, bgColor)

elif humidityValue > 20 and humidityValue < 70:
    bgColor = humidityIsOk
    screen.displayMessage("ok", black, bgColor)
    start_air_read_save()

else:
    bgColor = humidityIsHigh
    screen.displayMessage("high", black, bgColor)

print("bgColor= " + str(bgColor))
