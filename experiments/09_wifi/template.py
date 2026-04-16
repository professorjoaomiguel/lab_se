# Experimento 9 — Wi-Fi e Web Server
# Professor: Prof. Me. João Miguel Lac Roehe
# Aluno: ___________________________  Data: ___/___/______
#
# ---------------------------------------------------------------
# ETAPA 1 (Intermediária): Conecte ao Wi-Fi e imprima seu IP.
# ETAPA 2 (Final): Crie um servidor que mostre o valor do Potenciômetro.
# ---------------------------------------------------------------

# REFLEXÃO (Obrigatório):
# Qual a função técnica do 'Socket' em um servidor web? Como ele permite que 
# um navegador externo (celular) se comunique com o seu ESP32?
# Resposta: _____________________________________________________
# _______________________________________________________________

import network
import socket
from machine import ADC, Pin

# TODO: Preencha com os dados da rede local
SSID = "___"
PASSWORD = "___"

def conecta():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        pass
    print("IP:", wlan.ifconfig()[0])

# TODO: Implemente a lógica do servidor socket
conecta()
