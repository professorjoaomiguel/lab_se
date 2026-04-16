from machine import Pin, ADC
from time import sleep
from utils import media_amostras

lm35 = ADC(Pin(2))
lm35.atten(ADC.ATTN_11DB)
lm35.width(ADC.WIDTH_12BIT)

while True:
    # Usa média de 20 amostras para estabilizar a leitura
    leitura = media_amostras(lm35, n=20)
    
    tensao = (leitura / 4095) * 3.3
    temperatura = tensao / 0.01  # 10 mV por °C
    
    print("Temperatura (Média): {:.2f} °C".format(temperatura))
    sleep(1)
