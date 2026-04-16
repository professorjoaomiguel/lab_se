from machine import Pin, PWM
import time

# Configura o Buzzer no GPIO 5
buzzer = PWM(Pin(5))

def beep(freq, duracao):
    buzzer.freq(freq)
    buzzer.duty(512)
    time.sleep(duracao)
    buzzer.duty(0)

# Botões para controle
sw1 = Pin(18, Pin.IN, Pin.PULL_UP)
sw2 = Pin(17, Pin.IN, Pin.PULL_UP)

print("Sistema de Alarme Pronto.")

while True:
    if sw1.value() == 0:
        beep(440, 0.2)  # Nota Lá
    elif sw2.value() == 0:
        beep(880, 0.2)  # Nota Lá (oitava acima)
    time.sleep(0.05)
