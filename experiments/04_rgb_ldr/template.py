# Experimento 4 — RGB e PWM
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Faça o LED Verde (GPIO 10) brilhar com 50% (duty 512).
# ETAPA 2 (Final): Use map_value para brilho proporcional ao LDR.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Explique com suas palavras: Por que usamos a função map_value em vez de 
# apenas usar o valor direto do LDR no duty do PWM?
# Resposta: _____________________________________________________
# _______________________________________________________________

from machine import Pin, ADC, PWM
from time import sleep
from utils import map_value

led_verde = PWM(Pin(10), freq=1000)
ldr = ADC(Pin(1))

while True:
    valor_ldr = ldr.read()
    # TODO: Etapa 2 - brilho = map_value(valor_ldr, ...)
    # led_verde.duty(brilho)
    sleep(0.05)
