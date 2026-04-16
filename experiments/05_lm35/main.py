from machine import Pin, ADC
from time import sleep

lm35 = ADC(Pin(1))
lm35.atten(ADC.ATTN_11DB)
lm35.width(12)

while True:
    leitura = lm35.read()
    tensao = (leitura / 4095) * 3.3
    temperatura = tensao / 0.01  # LM35: 10 mV por °C
    print("Temperatura: {:.2f} °C".format(temperatura))
    sleep(1)
