# Experimento 6 — Dimer com Potenciômetro
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Exiba no Shell o valor do pot. em % (0-100).
# ETAPA 2 (Final): Controle o brilho do LED Azul (D12) com PWM.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Descreva o fluxo de dados deste experimento: como o valor analógico do 
# potenciômetro se transforma em brilho variável no LED?
# Resposta: _____________________________________________________
# _______________________________________________________________

from machine import ADC, Pin, PWM
from time import sleep
from utils import map_value

pot = ADC(Pin(36))
led = PWM(Pin(12), freq=1000)

while True:
    valor = pot.read()
    
    # TODO: Etapa 1 - porcento = (valor / 4095) * 100
    
    # TODO: Etapa 2 - brilho = map_value(valor, 0, 4095, 0, 1023)
    # led.duty(brilho)
    
    sleep(0.05)
