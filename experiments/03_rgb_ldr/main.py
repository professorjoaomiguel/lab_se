from machine import Pin, ADC, PWM
from time import sleep

led_green = PWM(Pin(10))
led_green.freq(1000)

led_red = PWM(Pin(13))
led_red.freq(1000)


def off():
    led_green.duty(0)
    led_red.duty(0)


ldr = ADC(Pin(1))
ldr.atten(ADC.ATTN_11DB)
ldr.width(ADC.WIDTH_12BIT)

while True:
    valor = ldr.read()
    print("LDR:", valor)
    if valor < 1200:
        intensidade = int((1200 - valor) / 1200 * 300)
        off()
        led_green.duty(intensidade)
    elif valor < 2600:
        intensidade = int((valor - 1200) / (2600 - 1200) * 1023)
        off()
        led_green.duty(intensidade)
    else:
        intensidade = int((valor - 2600) / (4095 - 2600) * 1023)
        off()
        led_red.duty(intensidade)
    sleep(0.1)
