import dht
from machine import Pin
import time

sensor = dht.DHT11(Pin(4))
led_aviso = Pin(13, Pin.OUT)

print("Monitor de Ambiente Iniciado...")

while True:
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        
        print("Temp: {}°C | Umid: {}%".format(t, h))
        
        # Alerta de baixa umidade (exemplo < 40%)
        if h < 40:
            led_aviso.on()
        else:
            led_aviso.off()
            
    except OSError as e:
        print("Falha na leitura do sensor.")
        
    time.sleep(2)
