# Experimento 9 — Contador de Eventos
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Contar quantas vezes cada botão foi pressionado.
#           Pressionar SW1 + SW2 ao mesmo tempo zera os contadores.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e observe os contadores no Shell.
#
# Referência de pinos:
#   SW1 → GPIO 18
#   SW2 → GPIO 17
# ---------------------------------------------------------------

from machine import Pin
from time import sleep

# TODO: Configure SW1 no GPIO 18 com Pull-Up
sw1 = Pin(___, Pin.___, Pin.___)

# TODO: Configure SW2 no GPIO 17 com Pull-Up
sw2 = Pin(___, Pin.___, Pin.___)

# TODO: Inicialize os contadores com zero
cont_sw1 = ___
cont_sw2 = ___

print("Contador pronto. SW1 e SW2 incrementam. SW1+SW2 zera.")

while True:
    v1 = sw1.value()
    v2 = sw2.value()

    # TODO: Se ambos pressionados (v1 == 0 e v2 == 0), zere os contadores
    if v1 == ___ and v2 == ___:
        cont_sw1 = ___
        cont_sw2 = ___
        print("Contadores zerados!")
        sleep(0.5)

    # TODO: Se apenas SW1 pressionado, incremente cont_sw1
    elif v1 == ___:
        cont_sw1 += ___
        print("SW1:", cont_sw1, "| SW2:", cont_sw2)
        sleep(0.2)

    # TODO: Se apenas SW2 pressionado, incremente cont_sw2
    elif v2 == ___:
        cont_sw2 += ___
        print("SW1:", cont_sw1, "| SW2:", cont_sw2)
        sleep(0.2)

    sleep(0.05)
