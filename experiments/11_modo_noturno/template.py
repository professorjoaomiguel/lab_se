# Experimento 11 — Modo Noturno Automático
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Controlar o brilho do LED verde (RGB) inversamente
#           à luminosidade lida pelo LDR — quanto menos luz,
#           mais brilhante o LED.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5, cubra ou ilumine o LDR e observe o LED.
#
# Referência de pinos:
#   LDR             → GPIO 1  (ADC, 0 = escuro, 4095 = muito iluminado)
#   LED verde (RGB) → GPIO 10 (PWM, duty 0–1023)
#
# Fórmula (relação inversa):
#   brilho = int((1 - valor / 4095) * 1023)
# ---------------------------------------------------------------

from machine import Pin, ADC, PWM
from time import sleep

# TODO: Configure o ADC no GPIO 1 com atenuação 11dB e resolução 12 bits
ldr = ADC(Pin(___))
ldr.atten(___)
ldr.width(___)

# TODO: Configure o LED verde RGB como PWM no GPIO 10, frequência 1000 Hz
led = PWM(Pin(___))
led.freq(___)

print("Modo noturno pronto. Cubra o LDR para aumentar o brilho.")

while True:
    # TODO: Leia o valor do LDR
    valor = ldr.___()

    # TODO: Calcule o brilho com relação inversa ao valor do LDR
    brilho = int((1 - valor / ___) * ___)

    # TODO: Aplique o brilho ao LED via duty
    led.___(brilho)

    print("LDR:", valor, "| Brilho:", brilho)
    sleep(0.1)
