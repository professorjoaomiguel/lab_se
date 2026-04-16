# Experimento 3 — LED RGB com LDR e PWM
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Controlar o brilho do LED verde ou vermelho proporcionalmente
#           à intensidade de luz lida pelo LDR.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e observe o Shell e o LED RGB.
#
# Referência de pinos:
#   LED verde (RGB) → GPIO 10 (PWM)
#   LED verm. (RGB) → GPIO 13 (PWM)
#   LDR             → GPIO 1  (ADC)
#
# Faixas de operação:
#   valor < 1200         → LED verde (pouca luz)
#   1200 <= valor < 2600 → LED verde (transição)
#   valor >= 2600        → LED vermelho (luz forte)
# ---------------------------------------------------------------

from machine import Pin, ADC, PWM
from time import sleep

# TODO: Configure led_green como PWM no GPIO 10, frequência 1000 Hz
led_green = PWM(Pin(___))
led_green.freq(___)

# TODO: Configure led_red como PWM no GPIO 13, frequência 1000 Hz
led_red = PWM(Pin(___))
led_red.freq(___)


def off():
    # TODO: Apague os dois LEDs definindo duty = 0
    led_green.duty(___)
    led_red.duty(___)


# TODO: Configure o ADC no GPIO 1 com atenuação 11dB e resolução 12 bits
ldr = ADC(Pin(___))
ldr.atten(___)
ldr.width(___)

while True:
    valor = ldr.read()
    print("LDR:", valor)

    if valor < 1200:
        # TODO: Calcule a intensidade proporcional para pouca luz e acenda led_green
        intensidade = int((1200 - valor) / 1200 * ___)
        off()
        led_green.duty(___)
    elif valor < 2600:
        # TODO: Calcule a intensidade proporcional na faixa de transição e acenda led_green
        intensidade = int((valor - 1200) / (2600 - 1200) * ___)
        off()
        led_green.duty(___)
    else:
        # TODO: Calcule a intensidade proporcional para luz forte e acenda led_red
        intensidade = int((valor - 2600) / (4095 - 2600) * ___)
        off()
        led_red.duty(___)

    sleep(0.1)
