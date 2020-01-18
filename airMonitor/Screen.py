# from sense_hat import SenseHat


class Screen:
    'SenseHat Screen (8x8 pixels)'

    def __init__(self):
        self.sense = SenseHat()
        self.message = ''

    def displayMessage(self, message, txtColor, bgColor):
        self.sense.show_message(message, text_colour=txtColor, back_colour=bgColor)
