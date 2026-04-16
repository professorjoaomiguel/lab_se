# Experimento 3 — LDR e Histerese
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Leia o LDR e imprima o valor bruto no Shell.
# ETAPA 2 (Final): Implemente a Histerese (Limiar Alto e Limiar Baixo).
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Como a utilização de dois limiares (Histerese) melhora a estabilidade 
# do sistema em comparação a um limiar único?
# Resposta: _____________________________________________________
# _______________________________________________________________

from machine import Pin, ADC
from time import sleep

ldr = ADC(Pin(1))
ldr.atten(ADC.ATTN_11DB)
led = Pin(13, Pin.OUT)

while True:
    valor = ldr.read()
    # TODO: Etapa 1 - Print valor
    
    # TODO: Etapa 2 - Se valor > Limiar_Alto -> Liga LED; Se valor < Limiar_Baixo -> Desliga
    
    sleep(0.1)
