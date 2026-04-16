from machine import ADC, Pin
from time import sleep

PINO_POT = 2
adc = ADC(Pin(PINO_POT))
try:
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
except:
    pass

print("Lendo potenciômetro no GPIO", PINO_POT)

while True:
    valor = adc.read()  # 0..4095
    por = int((valor / 4095) * 100)
    print("Bruto:", valor, " | ", por, "%")
    sleep(0.15)
