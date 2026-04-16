# Experimento 8 — Sensor DHT11 (Digital)
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Leia e exiba Temp/Umid no Shell.
# ETAPA 2 (Final): Se a umidade for < 40%, acenda o LED Vermelho (D13).
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Por que sensores digitais como o DHT11 são considerados mais "robustos" 
# em relação a ruídos elétricos do que sensores analógicos como o LM35?
# Resposta: _____________________________________________________
# _______________________________________________________________

import dht
from machine import Pin
import time

# TODO: Configure o sensor no GPIO 4
sensor = dht.DHT11(Pin(4))

while True:
    try:
        # TODO: Chame o método de medição
        sensor.measure()
        
        # TODO: Guarde temperatura e umidade em variáveis
        # t = sensor.temperature()
        
        # print("Temp:", t)
        
    except OSError:
        print("Erro no sensor")
        
    time.sleep(2)
