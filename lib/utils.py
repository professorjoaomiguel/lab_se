# utils.py — Funções utilitárias comuns
#
# Copie este arquivo para o ESP32 via Thonny (salve em "Dispositivo MicroPython")
# e importe com:  from utils import map_value, media_amostras

from time import sleep


def map_value(valor, in_min, in_max, out_min, out_max):
    """Mapeia 'valor' de uma faixa de entrada para uma faixa de saída.

    Exemplo:
        map_value(2048, 0, 4095, 0, 1023)  # => 511
    """
    return int((valor - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def media_amostras(adc, n=10, intervalo=0.01):
    """Retorna a média de 'n' leituras de um objeto ADC.

    Útil para suavizar ruídos em sensores analógicos (LDR, LM35, potenciômetro).

    Exemplo:
        from machine import ADC, Pin
        from utils import media_amostras
        ldr = ADC(Pin(1))
        ldr.atten(ADC.ATTN_11DB)
        valor = media_amostras(ldr)
    """
    total = 0
    for _ in range(n):
        total += adc.read()
        sleep(intervalo)
    return total // n


def debounce(pino, espera=0.05):
    """Aguarda o sinal de um pino estabilizar (debounce por software).

    Retorna True se o pino ainda estiver pressionado após 'espera' segundos.

    Exemplo:
        from machine import Pin
        from utils import debounce
        btn = Pin(18, Pin.IN, Pin.PULL_UP)
        if btn.value() == 0 and debounce(btn):
            print("Botão confirmado!")
    """
    sleep(espera)
    return pino.value() == 0
