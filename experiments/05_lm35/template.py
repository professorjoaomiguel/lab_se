# Experimento 5 — Sensor LM35
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Converta 'leitura' em 'tensao' (V).
# ETAPA 2 (Final): Use media_amostras() e exiba em Celsius.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Qual a importância de tirar a média de várias amostras (função media_amostras) 
# antes de exibir a temperatura final? O que acontece com a oscilação do valor?
# Resposta: _____________________________________________________
# _______________________________________________________________

from machine import Pin, ADC
from time import sleep
from utils import media_amostras

lm35 = ADC(Pin(2))
lm35.atten(ADC.ATTN_11DB)

while True:
    # TODO: Etapa 2 - leitura = media_amostras(lm35, 20)
    leitura = lm35.read()
    
    # TODO: Etapa 1 - tensao = (leitura / 4095) * 3.3
    
    # TODO: temperatura = tensao / 0.01
    
    # print("Temp: {:.1f} C".format(temperatura))
    sleep(1)
