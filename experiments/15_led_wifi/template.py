# Experimento 15 — Controle de LED via Web (Wi-Fi)
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Controlar D12 e D13 remotamente acessando uma página
#           HTML servida pelo próprio ESP32 via Wi-Fi.
#
# Instruções:
#   1. Preencha SSID e SENHA com as credenciais da sua rede Wi-Fi.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e anote o IP exibido no Shell.
#   5. Acesse http://<IP> em um navegador no mesmo Wi-Fi.
#
# Referência de pinos:
#   LED azul  (D12) → GPIO 12
#   LED verm. (D13) → GPIO 13
# ---------------------------------------------------------------

import network
import socket
from machine import Pin
from time import sleep

SSID = "___"    # TODO: Coloque o nome da sua rede Wi-Fi
SENHA = "___"   # TODO: Coloque a senha da sua rede Wi-Fi

# TODO: Configure led_D12 como saída no GPIO 12
led_D12 = Pin(___, Pin.___)

# TODO: Configure led_D13 como saída no GPIO 13
led_D13 = Pin(___, Pin.___)

# TODO: Crie e ative a interface STA (station) do Wi-Fi
sta = network.WLAN(network.___)
sta.active(___)
sta.connect(SSID, SENHA)

print("Conectando ao Wi-Fi...")
for _ in range(20):
    if sta.isconnected():
        break
    sleep(0.5)

if not sta.isconnected():
    print("Falha na conexão.")
    raise SystemExit

ip = sta.ifconfig()[0]
print("Conectado! Acesse http://{}".format(ip))

HTML = """\
HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
<!DOCTYPE html><html><head><meta charset="utf-8">
<title>ESP32 LEDs</title></head><body>
<h2>Controle de LEDs</h2>
<a href="/d12/on">D12 Ligar</a>
<a href="/d12/off">D12 Desligar</a><br>
<a href="/d13/on">D13 Ligar</a>
<a href="/d13/off">D13 Desligar</a>
</body></html>
"""

# TODO: Crie um socket TCP, faça bind na porta 80 e coloque em listen
srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("", ___))  # TODO: porta HTTP padrão
srv.listen(___)       # TODO: fila de conexões (ex.: 1)

while True:
    conn, addr = srv.accept()
    req = conn.recv(1024).decode()
    primeira_linha = req.split("\r\n")[0] if req else ""

    # TODO: Controle os LEDs conforme o caminho recebido
    if "/d12/on" in primeira_linha:
        led_D12.___()
    elif "/d12/off" in primeira_linha:
        led_D12.___()
    elif "/d13/on" in primeira_linha:
        led_D13.___()
    elif "/d13/off" in primeira_linha:
        led_D13.___()

    conn.send(HTML)
    conn.close()
