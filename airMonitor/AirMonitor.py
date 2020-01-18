import serial


class AirMonitor:
    'Check Air'

    def __init__(self):
        self.pmtwofive = 0
        self.pmten = 0

    def sensorPath(self, sensorPath):
        self.ser = serial.Serial(sensorPath)

    def read(self):
        data = []
        for index in range(0, 10):
            datum = self.ser.read()
            data.append(datum)

        self.pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
        self.pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10

        return self.pmtwofive, self.pmten
