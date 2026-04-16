from machine import Pin, ADC
from time import sleep

led_D12 = Pin(12, Pin.OUT)
led_D13 = Pin(13, Pin.OUT)

ldr = ADC(Pin(1))
ldr.atten(ADC.ATTN_11DB)
ldr.width(ADC.WIDTH_12BIT)

while True:
    valor = ldr.read()
    print("Luz:", valor)
    if valor > 2000:
        led_D13.on()
        led_D12.off()
    else:
        led_D12.on()
        led_D13.off()
    sleep(0.2)
