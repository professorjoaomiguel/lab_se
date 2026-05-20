# Experimento 09 — Wi-Fi e Servidor Web (IoT)
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
import time

# TODO: Preencha com os dados da rede local
SSID = "___"
PASSWORD = "___"

def conecta():
    # TODO: Etapa 1 - Configure o Wi-Fi no modo Station (STA_IF), ative e conecte.
    # Dica: use um loop 'while not wlan.isconnected():' com 'time.sleep(0.1)'
    # para aguardar a conexão sem travar o processador do ESP32.
    # No final, exiba o IP no terminal usando 'wlan.ifconfig()'.
    pass

# TODO: Implemente a lógica do servidor socket
conecta()
