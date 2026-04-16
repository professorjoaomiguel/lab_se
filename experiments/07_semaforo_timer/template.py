# Experimento 7 — Semáforo com Temporização
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Simular um semáforo usando D12 (verde) e D13 (vermelho)
#           com temporização precisa via machine.Timer.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e observe os LEDs e o Shell.
#
# Referência de pinos:
#   LED azul/verde (D12) → GPIO 12
#   LED vermelho   (D13) → GPIO 13
#
# Fases do semáforo:
#   0 → verde   (D12 aceso, D13 apagado) — 4000 ms
#   1 → amarelo (ambos apagados)         — 1000 ms
#   2 → vermelho(D12 apagado, D13 aceso) — 3000 ms
# ---------------------------------------------------------------

from machine import Pin, Timer

# TODO: Configure led_D12 como saída no GPIO 12
led_D12 = Pin(___, Pin.___)

# TODO: Configure led_D13 como saída no GPIO 13
led_D13 = Pin(___, Pin.___)

FASES = [
    (1, 0, 4000),
    (0, 0, 1000),
    (0, 1, 3000),
]

fase_atual = 0


def proxima_fase(t):
    global fase_atual
    # TODO: Desempacote FASES[fase_atual] em d12, d13 e duracao
    d12, d13, duracao = ___[___]

    # TODO: Aplique os valores aos LEDs
    led_D12.value(___)
    led_D13.value(___)

    print("Fase:", fase_atual, "| D12:", d12, "| D13:", d13)

    # TODO: Avance fase_atual para a próxima fase (circular)
    fase_atual = (___ + 1) % len(FASES)

    # TODO: Reinicie o timer com o período da fase atual (ONE_SHOT)
    t.init(period=___, mode=Timer.___, callback=___)


timer = Timer(0)
proxima_fase(timer)
