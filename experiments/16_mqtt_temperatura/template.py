# Experimento 16 — Monitoramento de Temperatura via MQTT
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Publicar a temperatura lida pelo LM35 num broker MQTT
#           público a cada 5 segundos.
#
# Instruções:
#   1. Preencha SSID e SENHA com as credenciais da sua rede Wi-Fi.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo.
#   4. Pressione F5. Use um cliente MQTT (ex.: MQTT Explorer) para
#      assinar o tópico labse/temperatura e ver os valores chegarem.
#
# Referência de pinos:
#   LM35 → GPIO 1 (ADC)
#
# Broker público: broker.hivemq.com, porta 1883
# Tópico:        labse/temperatura
# ---------------------------------------------------------------

import network
import socket  # necessário para criar o servidor TCP (mqtt_connect usa socket diretamente)
from machine import Pin, ADC
from time import sleep

SSID = "___"
SENHA = "___"

BROKER = "broker.hivemq.com"
PORTA = 1883
TOPICO = b"labse/temperatura"
CLIENT_ID = b"esp32_labse"

# TODO: Configure o ADC no GPIO 1 com atenuação 11dB e resolução 12 bits
lm35 = ADC(Pin(___))
lm35.atten(___)
lm35.width(___)


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


def mqtt_connect():
    sock = socket.socket()
    sock.connect(socket.getaddrinfo(BROKER, PORTA)[0][-1])
    cid = CLIENT_ID
    payload = (
        b"\x00\x04MQTT"
        b"\x04"
        b"\x02"
        b"\x00\x3c"
        + bytes([0, len(cid)]) + cid
    )
    header = b"\x10" + bytes([len(payload)])
    sock.send(header + payload)
    sock.recv(4)
    return sock


def mqtt_publish(sock, topico, mensagem):
    # TODO: Monte e envie o pacote PUBLISH ao broker
    tlen = len(topico)
    msg = bytes([0, tlen]) + topico + mensagem.encode()
    header = b"\x30" + bytes([len(msg)])
    sock.___(header + msg)  # TODO: método para enviar dados pelo socket


conectar_wifi()
sock = mqtt_connect()
print("MQTT conectado. Publicando em:", TOPICO.decode())

while True:
    leitura = lm35.read()
    tensao = (leitura / ___) * ___   # TODO: converta para tensão (0–3.3 V)
    temperatura = tensao / ___        # TODO: converta para °C (LM35: 10 mV/°C)
    msg = "{:.2f}".format(temperatura)
    mqtt_publish(sock, TOPICO, msg)
    print("Publicado:", msg, "°C")
    sleep(___)  # TODO: intervalo entre publicações (segundos)
