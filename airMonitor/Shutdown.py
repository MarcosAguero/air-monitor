# import os
# import time
# from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED


class Shutdown:
    """Shutdown Raspberry Pi"""

    def __init__(self, sense_hat, time, os):
        self.sense = sense_hat
        self.x = (2)  # shutdown variable
        self.time = time
        self.os = os

    def pushed_middle(self):
        self.x = 0
        self.sense.clear()
        print(str(self.x))
        self.sense.show_message("Apagar")
        self.os.system("sudo shutdown -P +1")
        # self.time.sleep(30)

    def pushed_up(self):
        self.x = 1
        self.sense.clear()
        print(str(self.x))
        self.sense.show_message("Cancelar")
        self.os.system("sudo shutdown -c")
        # self.time.sleep(30)
