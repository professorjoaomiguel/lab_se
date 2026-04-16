import network
import socket
from machine import Pin
from time import sleep

# ---------------------------------------------------------------
# Configuração Wi-Fi — preencha as credenciais da sua rede
SSID = "SEU_SSID"
SENHA = "SUA_SENHA"
# ---------------------------------------------------------------

led_D12 = Pin(12, Pin.OUT)
led_D13 = Pin(13, Pin.OUT)

# Conecta à rede Wi-Fi
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(SSID, SENHA)

print("Conectando ao Wi-Fi...")
for _ in range(20):
    if sta.isconnected():
        break
    sleep(0.5)

if not sta.isconnected():
    print("Falha na conexão. Verifique SSID e senha.")
    raise SystemExit

ip = sta.ifconfig()[0]
print("Conectado! Acesse http://{}".format(ip))

# Página HTML
HTML = """\
HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
<!DOCTYPE html><html><head><meta charset="utf-8">
<title>ESP32 LEDs</title>
<style>body{{font-family:sans-serif;text-align:center;margin-top:40px}}
a{{display:inline-block;padding:12px 24px;margin:8px;background:#0077cc;
color:#fff;border-radius:6px;text-decoration:none}}
a.off{{background:#cc3300}}</style></head>
<body><h2>Controle de LEDs — ESP32</h2>
<a href="/d12/on">D12 Ligar</a>
<a href="/d12/off" class="off">D12 Desligar</a><br>
<a href="/d13/on">D13 Ligar</a>
<a href="/d13/off" class="off">D13 Desligar</a>
</body></html>
"""

srv = socket.socket()
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(("", 80))
srv.listen(1)

while True:
    conn, addr = srv.accept()
    req = conn.recv(1024).decode()
    primeira_linha = req.split("\r\n")[0] if req else ""

    if "/d12/on" in primeira_linha:
        led_D12.on()
    elif "/d12/off" in primeira_linha:
        led_D12.off()
    elif "/d13/on" in primeira_linha:
        led_D13.on()
    elif "/d13/off" in primeira_linha:
        led_D13.off()

    conn.send(HTML)
    conn.close()
