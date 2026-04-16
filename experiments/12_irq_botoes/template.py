# Experimento 12 — Interrupções por Botão (IRQ)
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Reagir ao pressionamento de SW1 e SW2 usando interrupções
#           de hardware (Pin.irq), sem bloquear o loop principal.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5, pressione os botões e observe o Shell.
#
# Referência de pinos:
#   SW1 → GPIO 18
#   SW2 → GPIO 17
#
# Dica: use Pin.IRQ_FALLING para detectar a borda de descida
#       (botão pressionado = transição de HIGH para LOW).
# ---------------------------------------------------------------

from machine import Pin
from time import sleep

cont_sw1 = 0
cont_sw2 = 0


# TODO: Implemente o callback chamado quando SW1 for pressionado
def cb_sw1(p):
    global cont_sw1
    cont_sw1 += ___
    print("SW1 pressionado! Total SW1:", ___)


# TODO: Implemente o callback chamado quando SW2 for pressionado
def cb_sw2(p):
    global cont_sw2
    cont_sw2 += ___
    print("SW2 pressionado! Total SW2:", ___)


# TODO: Configure SW1 no GPIO 18 com Pull-Up
sw1 = Pin(___, Pin.___, Pin.___)

# TODO: Configure SW2 no GPIO 17 com Pull-Up
sw2 = Pin(___, Pin.___, Pin.___)

# TODO: Registre a IRQ de SW1 na borda de descida com handler cb_sw1
sw1.irq(trigger=Pin.___, handler=___)

# TODO: Registre a IRQ de SW2 na borda de descida com handler cb_sw2
sw2.irq(trigger=Pin.___, handler=___)

print("IRQ configurado. Pressione SW1 ou SW2.")

while True:
    sleep(1)
    print("Loop principal em execução... SW1:", cont_sw1, "SW2:", cont_sw2)
