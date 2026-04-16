import machine
import esp32
from machine import Pin
from time import sleep

sw1 = Pin(18, Pin.IN, Pin.PULL_UP)

TEMPO_SLEEP_S = 10  # segundos em deep sleep

print("Entrando em deep sleep por", TEMPO_SLEEP_S, "segundos.")
print("Ou pressione SW1 (GPIO 18) para acordar manualmente.")
sleep(1)  # pequena pausa para o serial imprimir

# Configura wake-up pelo pino SW1 (nível LOW = botão pressionado)
esp32.wake_on_ext0(pin=sw1, level=esp32.WAKEUP_ALL_LOW)

# Entra em deep sleep
machine.deepsleep(TEMPO_SLEEP_S * 1000)
