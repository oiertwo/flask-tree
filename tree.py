from gpiozero import LEDBoard, LED
from gpiozero.tools import random_values
from signal import pause
from time import sleep
import threading
from random import randint


tree = LEDBoard(*range(2,28),pwm=True)


class Random(threading.Thread):

    def __init__(self):
        super(Random, self).__init__()
        self._stop_event = threading.Event()
        self.mode = "random"

    def _random(self):
        for led in tree:
            led.value = randint(0, 1)
            sleep(0.01)
    def _onebyone(self):
        for led in tree:
            led.on()
            sleep(0.1)
            led.off()
            sleep(0.1)

    def _alloff(self):
        for led in tree:
            led.off()

    def run(self):
        while not self._stop_event.is_set():
            if self.mode == "random":
                #tree.close()
                self._random()
            elif self.mode == "onebyone":
                #tree.close()
                self._onebyone()
            else:
                #tree.close()
                self._alloff()


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
