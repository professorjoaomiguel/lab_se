from machine import Pin, Timer

led_D12 = Pin(12, Pin.OUT)
led_D13 = Pin(13, Pin.OUT)

estado = [False]  # lista para mutabilidade dentro do callback


def alternar(t):
    estado[0] = not estado[0]
    led_D12.value(estado[0])
    led_D13.value(not estado[0])


timer = Timer(0)
timer.init(period=500, mode=Timer.PERIODIC, callback=alternar)

print("Pisca-pisca com Timer iniciado. Loop principal livre.")

while True:
    # Loop principal pode executar outras tarefas enquanto o timer pisca
    pass
