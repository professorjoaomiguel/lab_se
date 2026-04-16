# Experimento 10 — Termostato com Indicador LED
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Ler a temperatura com o LM35 e acender D13 (vermelho)
#           quando a temperatura ultrapassar o limiar, ou D12 (azul)
#           quando estiver abaixo.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e observe o Shell e os LEDs.
#
# Referência de pinos:
#   LM35        → GPIO 1  (ADC)
#   LED azul D12  → GPIO 12
#   LED verm. D13 → GPIO 13
#
# Fórmulas:
#   tensão (V)      = leitura / 4095 × 3.3
#   temperatura (°C) = tensão / 0.01
# ---------------------------------------------------------------

from machine import Pin, ADC
from time import sleep

LIMIAR = ___  # TODO: Defina o limiar de temperatura em °C (ex.: 30.0)

# TODO: Configure o ADC no GPIO 1 com atenuação 11dB e resolução 12 bits
lm35 = ADC(Pin(___))
lm35.atten(___)
lm35.width(___)

# TODO: Configure led_D12 como saída no GPIO 12
led_D12 = Pin(___, Pin.___)

# TODO: Configure led_D13 como saída no GPIO 13
led_D13 = Pin(___, Pin.___)

print("Termostato pronto. Limiar:", LIMIAR, "°C")

while True:
    leitura = lm35.read()

    # TODO: Converta a leitura em tensão
    tensao = (leitura / ___) * ___

    # TODO: Converta a tensão em temperatura (LM35: 10 mV/°C)
    temperatura = tensao / ___

    # TODO: Se temperatura > LIMIAR, acenda D13 e apague D12; senão o contrário
    if temperatura > ___:
        led_D13.___()
        led_D12.___()
        estado = "ALTA"
    else:
        led_D12.___()
        led_D13.___()
        estado = "OK"

    print("Temp: {:.2f} °C | {}".format(temperatura, estado))
    sleep(1)
