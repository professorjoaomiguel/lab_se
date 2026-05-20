from machine import Pin
from time import sleep

sw1 = Pin(18, Pin.IN, Pin.PULL_UP)
sw2 = Pin(17, Pin.IN, Pin.PULL_UP)
led_azul = Pin(12, Pin.OUT)

print("Botões prontos...")

estado_led = False
led_azul.value(estado_led)

while True:
    if sw1.value() == 0:
        print("SW1 pressionado")
        estado_led = not estado_led  # Inverte o estado do LED
        led_azul.value(estado_led)
        sleep(0.2)  # debounce por software
    if sw2.value() == 0:
        print("SW2 pressionado")
        sleep(0.2)  # debounce
    sleep(0.05)
