from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep
import threading

class Random(threading.Thread):

    def __init__(self):
        super(Random, self).__init__()
        self._stop_event = threading.Event()


    def run():
        while not self._stop_event.is_set():
            tree = LEDBoard(*range(2,28),pwm=True)
            for led in tree:
                led.source_delay = 0.1
                led.source = random_values()

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

    def run():
        tree = LEDBoard(*range(2,28),pwm=True)

        while not self._stop_event.is_set():
            for led in tree:
                if not self._stop_event.is_set():
                    led.on()
                    sleep(0.1)
                    led.off()
                    sleep(0.1)
