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
    
    # Lógica com Histerese
    if valor > 2200:
        led_D13.on()   # Liga Vermelho com luz forte
        led_D12.off()
    elif valor < 1800:
        led_D12.on()   # Liga Azul com luz fraca
        led_D13.off()
    
    sleep(0.1)
