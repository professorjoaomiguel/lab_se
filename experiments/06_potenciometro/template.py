# Experimento 6 — Dimer com Potenciômetro
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Ler o potenciômetro e exibir o valor bruto e o percentual
#           correspondente no monitor serial.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5, gire o potenciômetro e observe os valores no Shell.
#
# Referência de pinos:
#   Potenciômetro → GPIO 2 (ADC)
#
# Dica: para controlar o brilho de um LED com PWM, mapeie o valor (0–4095)
#       para a escala do duty (0–1023):
#           duty = int((valor / 4095) * 1023)
# ---------------------------------------------------------------

from machine import ADC, Pin
from time import sleep

PINO_POT = ___  # TODO: Defina o número do GPIO do potenciômetro

# TODO: Configure o ADC no pino do potenciômetro
adc = ADC(Pin(___))
try:
    adc.atten(___)
    adc.width(___)
except:
    pass

print("Lendo potenciômetro no GPIO", PINO_POT)

while True:
    # TODO: Leia o valor bruto do ADC (0–4095)
    valor = adc.___()

    # TODO: Calcule o percentual (0–100) a partir do valor bruto
    por = int((valor / ___) * ___)

    print("Bruto:", valor, " | ", por, "%")
    sleep(0.15)
