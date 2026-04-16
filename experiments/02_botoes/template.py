# Experimento 2 — Botões
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Imprima "Botão pressionado" ao apertar SW1.
# ETAPA 2 (Final): Use o botão SW1 para ligar/apagar o LED Azul (D12).
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# O que aconteceria se não usássemos o 'sleep(0.2)' (debounce) após detectar 
# o pressionamento do botão? Como isso afetaria a lógica de 'Toggle'?
# Resposta: _____________________________________________________
# _______________________________________________________________

from machine import Pin
from time import sleep

sw1 = Pin(18, Pin.IN, Pin.PULL_UP)
led = Pin(12, Pin.OUT)

estado_led = False

while True:
    if sw1.value() == 0:
        # TODO: Etapa 1 - Print
        # TODO: Etapa 2 - Lógica de Toggle (inverter estado_led)
        sleep(0.2) # Debounce
    sleep(0.01)
