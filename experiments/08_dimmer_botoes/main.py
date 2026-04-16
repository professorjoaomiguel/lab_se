from machine import Pin, PWM
from time import sleep

sw1 = Pin(18, Pin.IN, Pin.PULL_UP)   # aumenta brilho
sw2 = Pin(17, Pin.IN, Pin.PULL_UP)   # diminui brilho

led = PWM(Pin(10))  # LED verde do RGB
led.freq(1000)

PASSO = 64   # incremento/decremento de brilho (0–1023)
brilho = 512

led.duty(brilho)
print("Dimmer pronto. SW1 aumenta, SW2 diminui.")
print("Brilho inicial:", brilho)

while True:
    if sw1.value() == 0:
        brilho = min(1023, brilho + PASSO)
        led.duty(brilho)
        print("Brilho:", brilho)
        sleep(0.2)  # debounce
    if sw2.value() == 0:
        brilho = max(0, brilho - PASSO)
        led.duty(brilho)
        print("Brilho:", brilho)
        sleep(0.2)  # debounce
    sleep(0.05)
