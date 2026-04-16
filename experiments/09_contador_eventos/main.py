from machine import Pin
from time import sleep

sw1 = Pin(18, Pin.IN, Pin.PULL_UP)
sw2 = Pin(17, Pin.IN, Pin.PULL_UP)

cont_sw1 = 0
cont_sw2 = 0

print("Contador pronto. SW1 e SW2 incrementam contadores.")
print("Pressione SW1 + SW2 ao mesmo tempo para zerar.")

while True:
    v1 = sw1.value()
    v2 = sw2.value()

    if v1 == 0 and v2 == 0:
        cont_sw1 = 0
        cont_sw2 = 0
        print("Contadores zerados!")
        sleep(0.5)  # evita múltiplos resets

    elif v1 == 0:
        cont_sw1 += 1
        print("SW1:", cont_sw1, "| SW2:", cont_sw2)
        sleep(0.2)  # debounce

    elif v2 == 0:
        cont_sw2 += 1
        print("SW1:", cont_sw1, "| SW2:", cont_sw2)
        sleep(0.2)  # debounce

    sleep(0.05)
