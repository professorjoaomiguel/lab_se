# Experimento 5 — Sensor de Temperatura LM35
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Medir a temperatura ambiente com o sensor LM35 e
#           exibir o valor em graus Celsius no monitor serial.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e observe as leituras no Shell.
#
# Referência de pinos:
#   LM35 → GPIO 1 (ADC)
#
# Fórmulas:
#   tensão (V)      = leitura / 4095 × 3.3
#   temperatura (°C) = tensão / 0.01    (LM35: 10 mV por °C)
# ---------------------------------------------------------------

from machine import Pin, ADC
from time import sleep

# TODO: Configure o ADC no GPIO 1 com atenuação 11dB e resolução 12 bits
lm35 = ADC(Pin(___))
lm35.atten(___)
lm35.width(___)

while True:
    # TODO: Leia o valor bruto do ADC
    leitura = lm35.___()

    # TODO: Converta a leitura em tensão (0–3.3 V)
    tensao = (leitura / ___) * ___

    # TODO: Converta a tensão em temperatura usando a fórmula do LM35
    temperatura = tensao / ___

    print("Temperatura: {:.2f} °C".format(temperatura))
    sleep(1)
