from machine import Pin
from time import sleep

cont_sw1 = 0
cont_sw2 = 0


def cb_sw1(p):
    global cont_sw1
    cont_sw1 += 1
    print("SW1 pressionado! Total SW1:", cont_sw1)


def cb_sw2(p):
    global cont_sw2
    cont_sw2 += 1
    print("SW2 pressionado! Total SW2:", cont_sw2)


sw1 = Pin(18, Pin.IN, Pin.PULL_UP)
sw2 = Pin(17, Pin.IN, Pin.PULL_UP)

# IRQ acionado na borda de descida (botão pressionado = LOW)
sw1.irq(trigger=Pin.IRQ_FALLING, handler=cb_sw1)
sw2.irq(trigger=Pin.IRQ_FALLING, handler=cb_sw2)

print("IRQ configurado. Pressione SW1 ou SW2.")

while True:
    # Loop principal fica livre para outras tarefas
    sleep(1)
    print("Loop principal em execução... SW1:", cont_sw1, "SW2:", cont_sw2)
