import network
import socket
from machine import Pin, ADC
from time import sleep

# ---------------------------------------------------------------
# Configuração Wi-Fi
SSID = "SEU_SSID"
SENHA = "SUA_SENHA"

# Broker MQTT público (sem autenticação)
BROKER = "broker.hivemq.com"
PORTA = 1883
TOPICO = b"labse/temperatura"
CLIENT_ID = b"esp32_labse"
# ---------------------------------------------------------------

lm35 = ADC(Pin(1))
lm35.atten(ADC.ATTN_11DB)
lm35.width(ADC.WIDTH_12BIT)


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
    """Conexão MQTT manual via socket (sem biblioteca externa)."""
    sock = socket.socket()
    sock.connect(socket.getaddrinfo(BROKER, PORTA)[0][-1])

    # Monta pacote CONNECT
    cid = CLIENT_ID
    payload = (
        b"\x00\x04MQTT"   # protocolo
        b"\x04"            # versão 3.1.1
        b"\x02"            # flags: clean session
        b"\x00\x3c"        # keep-alive 60 s
        + bytes([0, len(cid)]) + cid
    )
    header = b"\x10" + bytes([len(payload)])
    sock.send(header + payload)
    sock.recv(4)  # CONNACK
    return sock


def mqtt_publish(sock, topico, mensagem):
    """Publica uma mensagem no tópico."""
    tlen = len(topico)
    msg = bytes([0, tlen]) + topico + mensagem.encode()
    header = b"\x30" + bytes([len(msg)])
    sock.send(header + msg)


conectar_wifi()
sock = mqtt_connect()
print("MQTT conectado. Publicando em:", TOPICO.decode())

while True:
    leitura = lm35.read()
    tensao = (leitura / 4095) * 3.3
    temperatura = tensao / 0.01
    msg = "{:.2f}".format(temperatura)
    mqtt_publish(sock, TOPICO, msg)
    print("Publicado:", msg, "°C")
    sleep(5)
