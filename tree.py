from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause
from time import sleep

def random():
    tree = LEDBoard(*range(2,28),pwm=True)
    for led in tree:
        led.source_delay = 0.1
        led.source = random_values()

def onebyone():
    tree = LEDBoard(*range(2,28),pwm=True)
    for led in tree:
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)
