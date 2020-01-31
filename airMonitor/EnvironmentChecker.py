# from sense_hat import SenseHat
class EnvironmentChecker:
    'Check the Environment - Humidity , Temperature, Pression'

    def __init__(self, sense):
        self.sense = sense
        self.humidityValue = 0
        self.temperatureValue = 0

    def get_humidity_round_by(self, decimal_num):
        self.humidityValue = self.sense.get_humidity()
        # Round the values to one decimal place
        return round(self.humidityValue, decimal_num)

    def get_humidity(self):
        return self.humidityValue

    def get_temperature_round_by(self, decimal_num):
        self.temperatureValue = self.sense.get_temperature()
        # Round the values to one decimal place
        return round(self.humidityValue, decimal_num)

    def get_temperature(self):
        return self.temperatureValue

    def get_pressure_round_by(self, decimal_num):
        self.pressureValue = self.sense.get_pressure()
        # Round the values to one decimal place
        return round(self.humidityValue, decimal_num)

    def get_temperature(self):
        return self.pressureValue
