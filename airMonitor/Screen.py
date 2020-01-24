# from sense_hat import SenseHat


class Screen:
    'SenseHat Screen (8x8 pixels)'

    def __init__(self, sense):
        self.sense = sense
        self.message = ''

    def displayMessage(self, message, txtColor, bgColor):
        self.sense.show_message(message, text_colour=txtColor, back_colour=bgColor)
