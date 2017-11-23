from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep
import threading
from random import randint

class Random(threading.Thread):

    def __init__(self):
        super(Random, self).__init__()
        self._stop_event = threading.Event()
        self.mode = "random"
        self.tree = LEDBoard(*range(2,28),pwm=True)

    def run(self):
        while not self._stop_event.is_set():
            if self.mode == "random":
                for led in self.tree:
                    if not (self.mode == "random"):
                        break
                    #led.source_delay = 0.1
                    led.value = randint(0, 1)
            else:
                for led in self.tree:
                    if self.mode == "random":
                        break
                    led.on()
                    sleep(0.1)
                    led.off()
                    sleep(0.1)

    def stop(self, timeout):
        self._stop_event.set()
        self.join(timeout)

class Onebyone(threading.Thread):

    def __init__(self):
        super(Onebyone, self).__init__()
        self._stop_event = threading.Event()

    def stop(self, timeout):
        self._stop_event.set()
        self.join(timeout)

    def run(self):
        tree = LEDBoard(*range(2,28),pwm=True)

        while not self._stop_event.is_set():
            for led in tree:
                if not self._stop_event.is_set():
                    led.on()
                    sleep(0.1)
                    led.off()
                    sleep(0.1)
