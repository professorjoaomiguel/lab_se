from machine import Pin, ADC, PWM
from time import sleep
from utils import map_value

led_green = PWM(Pin(10))
led_green.freq(1000)

led_red = PWM(Pin(9))
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
    
    if valor < 1500:
        # Pouca luz: LED verde brilha inversamente à luz
        intensidade = map_value(valor, 0, 1500, 1023, 0)
        off()
        led_green.duty(intensidade)
    elif valor < 3000:
        # Transição: LED verde brilha proporcionalmente à luz
        intensidade = map_value(valor, 1500, 3000, 0, 1023)
        off()
        led_green.duty(intensidade)
    else:
        # Muita luz: LED vermelho brilha proporcionalmente à luz
        intensidade = map_value(valor, 3000, 4095, 0, 1023)
        off()
        led_red.duty(intensidade)
        
    sleep(0.1)
