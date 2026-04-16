# Experimento 1 — Botões
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Reconhecer qual botão (SW1 ou SW2) foi pressionado no Shield.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 para executar e observe o Shell.
#
# Referência de pinos:
#   SW1 → GPIO 18
#   SW2 → GPIO 17
# ---------------------------------------------------------------

from machine import Pin
from time import sleep

# TODO: Configure SW1 como entrada com Pull-Up interno no GPIO 18
sw1 = Pin(___, Pin.___, Pin.___)

# TODO: Configure SW2 como entrada com Pull-Up interno no GPIO 17
sw2 = Pin(___, Pin.___, Pin.___)

print("Botões prontos...")

while True:
    # TODO: Verifique se SW1 foi pressionado (valor == 0) e imprima uma mensagem
    if sw1.value() == ___:
        print("___")
        sleep(0.2)  # debounce

    # TODO: Verifique se SW2 foi pressionado (valor == 0) e imprima uma mensagem
    if sw2.value() == ___:
        print("___")
        sleep(0.2)  # debounce

    sleep(0.05)
