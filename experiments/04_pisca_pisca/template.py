# Experimento 4 — Pisca-pisca com LEDs
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Piscar alternadamente os LEDs D12 e D13 do Shield.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e observe os LEDs piscando.
#
# Referência de pinos:
#   LED azul  (D12) → GPIO 12
#   LED verm. (D13) → GPIO 13
# ---------------------------------------------------------------

from machine import Pin
from time import sleep

# TODO: Configure led_D12 como saída no GPIO 12
led_D12 = Pin(___, Pin.___)

# TODO: Configure led_D13 como saída no GPIO 13
led_D13 = Pin(___, Pin.___)

while True:
    # TODO: Acenda D12, apague D13 e aguarde 0.5 s
    led_D12.___()
    led_D13.___()
    sleep(___)

    # TODO: Apague D12, acenda D13 e aguarde 0.5 s
    led_D12.___()
    led_D13.___()
    sleep(___)
