from machine import Pin, Timer

led_D12 = Pin(12, Pin.OUT)  # verde/azul
led_D13 = Pin(13, Pin.OUT)  # vermelho

# Sequência: (D12, D13, duração_ms)
FASES = [
    (1, 0, 4000),   # verde: D12 aceso, D13 apagado
    (0, 0, 1000),   # amarelo: ambos apagados (sem LED amarelo no shield)
    (0, 1, 3000),   # vermelho: D12 apagado, D13 aceso
]

fase_atual = 0


def proxima_fase(t):
    global fase_atual
    d12, d13, duracao = FASES[fase_atual]
    led_D12.value(d12)
    led_D13.value(d13)
    print("Fase:", fase_atual, "| D12:", d12, "| D13:", d13)
    fase_atual = (fase_atual + 1) % len(FASES)
    t.init(period=duracao, mode=Timer.ONE_SHOT, callback=proxima_fase)


timer = Timer(0)
# Inicia imediatamente com a primeira fase
proxima_fase(timer)
