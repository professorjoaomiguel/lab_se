from machine import Pin, ADC
from time import sleep

led_vermelho = Pin(13, Pin.OUT)

ldr = ADC(Pin(1))
ldr.atten(ADC.ATTN_11DB)
ldr.width(ADC.WIDTH_12BIT)

print("Luz de Emergência com Histerese Iniciada...")

while True:
    valor = ldr.read()
    print("LDR (Luz):", valor)
    
    # Histerese: liga o LED Vermelho no escuro (< 1800) e desliga no claro (> 2200)
    if valor < 1800:
        led_vermelho.on()   # Liga no escuro
    elif valor > 2200:
        led_vermelho.off()  # Apaga na claridade
    
    sleep(0.1)
