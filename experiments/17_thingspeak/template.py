# Experimento 17 — Dashboard no ThingSpeak
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Enviar temperatura (LM35) e luminosidade (LDR) para o
#           ThingSpeak via HTTP e visualizar gráficos em tempo real.
#
# Instruções:
#   1. Crie uma conta em https://thingspeak.com e um canal com 2 campos.
#   2. Copie a Write API Key do canal e cole em WRITE_API_KEY.
#   3. Preencha SSID e SENHA.
#   4. Preencha os espaços marcados com TODO.
#   5. Salve como main.py no dispositivo e pressione F5.
#   6. Abra o canal no ThingSpeak e observe os gráficos atualizando.
#
# Referência de pinos:
#   LM35 / LDR → GPIO 1 (ADC) — leituras alternadas
#
# Atenção: ThingSpeak aceita no mínimo 15 s entre atualizações.
# ---------------------------------------------------------------

import network
import urequests
from machine import Pin, ADC
from time import sleep

SSID = "___"
SENHA = "___"
WRITE_API_KEY = "___"  # TODO: cole aqui sua Write API Key
URL = "https://api.thingspeak.com/update"

# TODO: Configure o ADC no GPIO 1 com atenuação 11dB e resolução 12 bits
lm35 = ADC(Pin(___))
lm35.atten(___)
lm35.width(___)

ldr = ADC(Pin(___))
ldr.atten(___)
ldr.width(___)


def conectar_wifi():
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(SSID, SENHA)
    print("Conectando ao Wi-Fi...")
    for _ in range(20):
        if sta.isconnected():
            break
        sleep(0.5)
    if not sta.isconnected():
        raise OSError("Sem conexão Wi-Fi")
    print("Wi-Fi OK:", sta.ifconfig()[0])


conectar_wifi()
print("Enviando dados ao ThingSpeak a cada 15 s...")

while True:
    leitura_temp = lm35.read()
    # TODO: Converta leitura_temp para temperatura em °C
    tensao = (leitura_temp / ___) * ___
    temperatura = tensao / ___

    # TODO: Leia o valor do LDR
    leitura_ldr = ldr.___()

    # TODO: Monte a URL com os parâmetros api_key, field1 e field2
    params = "?api_key={}&field1={:.2f}&field2={}".format(
        ___, ___, ___
    )
    try:
        r = urequests.___(URL + params)  # TODO: método HTTP de leitura
        print("Enviado | Temp: {:.2f} °C | LDR: {} | Entry: {}".format(
            temperatura, leitura_ldr, r.text))
        r.close()
    except Exception as e:
        print("Erro ao enviar:", e)

    sleep(___)  # TODO: aguarde o intervalo mínimo do ThingSpeak (segundos)
