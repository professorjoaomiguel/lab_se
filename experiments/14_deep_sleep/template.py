# Experimento 14 — Deep Sleep com Wake-up por Botão
# Aluno: ___________________________  Data: ___/___/______
#
# Objetivo: Colocar o ESP32 em deep sleep para economizar energia
#           e acordá-lo ao pressionar SW1 (GPIO 18) ou após um tempo.
#
# Instruções:
#   1. Abra este arquivo no Thonny.
#   2. Preencha os espaços marcados com TODO.
#   3. Salve como main.py no dispositivo (Arquivo → Salvar como → Dispositivo MicroPython).
#   4. Pressione F5. O ESP32 dormirá e acordará ao pressionar SW1.
#
# Referência de pinos:
#   SW1 → GPIO 18 (wake-up externo EXT0)
#
# Atenção: após machine.deepsleep() o ESP32 reinicia completamente.
#          Use boot.py para detectar a causa do wake-up se necessário.
# ---------------------------------------------------------------

import machine
import esp32
from machine import Pin
from time import sleep

# TODO: Configure SW1 no GPIO 18 com Pull-Up
sw1 = Pin(___, Pin.___, Pin.___)

TEMPO_SLEEP_S = ___  # TODO: Defina o tempo de deep sleep em segundos (ex.: 10)

print("Entrando em deep sleep por", TEMPO_SLEEP_S, "segundos.")
print("Pressione SW1 (GPIO 18) para acordar antes.")
sleep(1)

# TODO: Configure o wake-up externo EXT0 no pino sw1, nível WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin=___, level=esp32.___)

# TODO: Entre em deep sleep pelo tempo configurado (em milissegundos)
machine.deepsleep(___ * 1000)
