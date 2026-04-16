from machine import Pin
from time import sleep

sw1 = Pin(18, Pin.IN, Pin.PULL_UP)
sw2 = Pin(17, Pin.IN, Pin.PULL_UP)

print("Botões prontos...")

while True:
    if sw1.value() == 0:
        print("SW1 pressionado")
        sleep(0.2)  # debounce
    if sw2.value() == 0:
        print("SW2 pressionado")
        sleep(0.2)  # debounce
    sleep(0.05)
