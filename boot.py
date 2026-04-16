# boot.py — Inicialização do ESP32
#
# Este arquivo é executado automaticamente pelo MicroPython
# ANTES do main.py toda vez que a placa é ligada ou reiniciada.
#
# Use este arquivo para configurações globais do sistema,
# como conexão Wi-Fi, configuração de frequência de clock, etc.
# Para os experimentos deste laboratório, nenhuma alteração
# é necessária aqui.

import gc

# Libera memória não utilizada antes de iniciar o programa principal
gc.collect()
