# Experimento 07 — Buzzer e Frequência
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Faça o buzzer emitir um som fixo por 1s.
# ETAPA 2 (Final): Crie dois tons diferentes, um para cada botão.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Qual a diferença técnica entre controlar um LED (brilho) e um Buzzer (som) 
# usando PWM no MicroPython? O que o parâmetro 'freq' altera no som?
# Resposta: _____________________________________________________
# _______________________________________________________________

from machine import Pin, PWM
import time

# TODO: Configure o Buzzer (GPIO 5) como PWM
buzzer = PWM(Pin(5))

# TODO: Configure SW1 e SW2
sw1 = Pin(18, Pin.IN, Pin.PULL_UP)

# TODO: Etapa 1 - Faça o buzzer emitir um som fixo por 1s (fora do loop)
# (Dica: configure a frequência, ligue com duty 512, aguarde 1s e desligue com duty 0)

while True:
    # TODO: Se SW1 pressionado, buzzer.freq(440) e duty(512)
    # TODO: Senão, duty(0)
    time.sleep(0.1)
