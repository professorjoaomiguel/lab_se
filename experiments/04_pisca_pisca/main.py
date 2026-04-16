from machine import Pin
from time import sleep

led_D12 = Pin(12, Pin.OUT)
led_D13 = Pin(13, Pin.OUT)

while True:
    led_D12.on()
    led_D13.off()
    sleep(0.5)
    led_D12.off()
    led_D13.on()
    sleep(0.5)
