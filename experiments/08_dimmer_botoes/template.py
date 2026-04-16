# Experimento 8 — Dimmer por Botões
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Usar SW1 para aumentar e SW2 para diminuir o brilho
#           do LED verde (RGB) via PWM.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5, pressione SW1/SW2 e observe o LED e o Shell.
#
# Referência de pinos:
#   SW1 (aumenta) → GPIO 18
#   SW2 (diminui) → GPIO 17
#   LED verde RGB → GPIO 10 (PWM, duty 0–1023)
# ---------------------------------------------------------------

from machine import Pin, PWM
from time import sleep

# TODO: Configure SW1 como entrada com Pull-Up no GPIO 18
sw1 = Pin(___, Pin.___, Pin.___)

# TODO: Configure SW2 como entrada com Pull-Up no GPIO 17
sw2 = Pin(___, Pin.___, Pin.___)

# TODO: Configure o LED verde RGB como PWM no GPIO 10, frequência 1000 Hz
led = PWM(Pin(___))
led.freq(___)

PASSO = ___  # TODO: Defina o passo de incremento/decremento (sugestão: 64)
brilho = 512

led.duty(brilho)
print("Dimmer pronto. SW1 aumenta, SW2 diminui.")

while True:
    if sw1.value() == ___:  # TODO: Valor quando botão pressionado
        # TODO: Aumente o brilho, limitando ao máximo (1023)
        brilho = min(___, brilho + ___)
        led.duty(brilho)
        print("Brilho:", brilho)
        sleep(0.2)

    if sw2.value() == ___:  # TODO: Valor quando botão pressionado
        # TODO: Diminua o brilho, limitando ao mínimo (0)
        brilho = max(___, brilho - ___)
        led.duty(brilho)
        print("Brilho:", brilho)
        sleep(0.2)

    sleep(0.05)
