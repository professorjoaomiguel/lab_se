# Experimento 2 — Fotocélula e LEDs
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Acender o LED vermelho (D13) quando a luz for intensa (> 2000)
#           e o LED azul (D12) quando a luz for fraca.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e observe o Shell e os LEDs.
#
# Referência de pinos:
#   LED azul  (D12) → GPIO 12
#   LED verm. (D13) → GPIO 13
#   LDR             → GPIO 1 (ADC)
# ---------------------------------------------------------------

from machine import Pin, ADC
from time import sleep

# TODO: Configure led_D12 como saída no GPIO 12
led_D12 = Pin(___, Pin.___)

# TODO: Configure led_D13 como saída no GPIO 13
led_D13 = Pin(___, Pin.___)

# TODO: Configure o ADC no GPIO 1 com atenuação 11dB e resolução 12 bits
ldr = ADC(Pin(___))
ldr.atten(___)
ldr.width(___)

while True:
    # TODO: Leia o valor do LDR e guarde em 'valor'
    valor = ldr.___()
    print("Luz:", valor)

    # TODO: Se valor > 2000, acenda D13 e apague D12; senão, acenda D12 e apague D13
    if valor > ___:
        led_D13.___()
        led_D12.___()
    else:
        led_D12.___()
        led_D13.___()

    sleep(0.2)
