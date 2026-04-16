# Experimento 1 — Pisca-pisca com LEDs
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Faça apenas o LED Azul (D12) piscar.
# ETAPA 2 (Final): Faça os LEDs D12 e D13 piscarem alternadamente.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Por que o comando 'sleep' é essencial em um loop infinito que controla LEDs?
# O que aconteceria com o consumo de CPU e a percepção visual se ele fosse removido?
# Resposta: _____________________________________________________
# _______________________________________________________________

from machine import Pin
from time import sleep

# TODO: Configure os pinos 12 e 13 como saída
led_azul = Pin(12, Pin.OUT)
led_vermelho = Pin(13, Pin.OUT)

while True:
    # --- Início da Etapa 2 ---
    led_azul.on()
    led_vermelho.off()
    sleep(0.5)
    
    led_azul.off()
    led_vermelho.on()
    sleep(0.5)
