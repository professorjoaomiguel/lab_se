import network
import urequests
from machine import Pin, ADC
from time import sleep

# ---------------------------------------------------------------
# Configuração Wi-Fi
SSID = "SEU_SSID"
SENHA = "SUA_SENHA"

# ThingSpeak — crie um canal em https://thingspeak.com e copie a Write API Key
WRITE_API_KEY = "SUA_WRITE_API_KEY"
URL = "https://api.thingspeak.com/update"
# field1 = temperatura (LM35), field2 = luminosidade (LDR)
# ---------------------------------------------------------------

lm35 = ADC(Pin(1))
lm35.atten(ADC.ATTN_11DB)
lm35.width(ADC.WIDTH_12BIT)

ldr = ADC(Pin(1))  # compartilha GPIO 1; leituras alternadas
ldr.atten(ADC.ATTN_11DB)
ldr.width(ADC.WIDTH_12BIT)


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
    tensao = (leitura_temp / 4095) * 3.3
    temperatura = tensao / 0.01

    leitura_ldr = ldr.read()

    params = "?api_key={}&field1={:.2f}&field2={}".format(
        WRITE_API_KEY, temperatura, leitura_ldr
    )
    try:
        r = urequests.get(URL + params)
        print("Enviado | Temp: {:.2f} °C | LDR: {} | Entry: {}".format(
            temperatura, leitura_ldr, r.text))
        r.close()
    except Exception as e:
        print("Erro ao enviar:", e)

    sleep(15)  # ThingSpeak aceita no mínimo 15 s entre atualizações
