# Experimento 13 — Pisca-pisca com Timer (sem sleep)
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Piscar os LEDs D12 e D13 alternadamente usando machine.Timer
#           sem bloquear o loop principal com sleep().
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5 e observe os LEDs piscando e o Shell imprimindo.
#
# Referência de pinos:
#   LED azul  (D12) → GPIO 12
#   LED verm. (D13) → GPIO 13
#
# Dica: use Timer.PERIODIC para disparar o callback repetidamente.
# ---------------------------------------------------------------

from machine import Pin, Timer

# TODO: Configure led_D12 como saída no GPIO 12
led_D12 = Pin(___, Pin.___)

# TODO: Configure led_D13 como saída no GPIO 13
led_D13 = Pin(___, Pin.___)

estado = [False]  # lista para mutabilidade dentro do callback


def alternar(t):
    # TODO: Inverta o estado atual (True/False)
    estado[0] = not estado[___]

    # TODO: Aplique o estado aos LEDs (D12 = estado, D13 = oposto)
    led_D12.value(estado[___])
    led_D13.value(not estado[___])


# TODO: Crie um Timer com id=0
timer = Timer(___)

# TODO: Inicialize o timer com período 500 ms, modo PERIODIC e callback alternar
timer.init(period=___, mode=Timer.___, callback=___)

print("Pisca-pisca com Timer iniciado. Loop principal livre.")

while True:
    pass  # Loop livre — o timer cuida do pisca-pisca
