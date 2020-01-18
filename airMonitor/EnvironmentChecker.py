# from sense_hat import SenseHat
class EnvironmentChecker:
    'Check the Environment - Humidity , Temperature, Pression'

    def __init__(self):
        self.sense = SenseHat()
        self.humidityValue = 0

    def get_humidity_round_by(self, decimal_num):
        self.humidityValue = self.sense.get_humidity()
        # Round the values to one decimal place
        return round(self.humidityValue, decimal_num)

    def get_humidity(self):
        return self.humidityValue
