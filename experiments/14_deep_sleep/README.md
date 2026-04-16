# Experimento 14 — Deep Sleep com Wake-up por Botão

## Objetivo

Colocar o ESP32 em **deep sleep** para reduzir drasticamente o consumo de energia e acordá-lo ao pressionar SW1 (wake-up externo EXT0) ou após um tempo configurado — comportamento fundamental para dispositivos IoT alimentados por bateria.

## Componentes Utilizados

| Componente | Pino GPIO |
|------------|-----------|
| Botão SW1  | GPIO 18   |

## Como Funciona

O `machine.deepsleep()` desliga quase todos os circuitos do ESP32, mantendo apenas o RTC (Real-Time Clock) e os pinos de wake-up ativos. O consumo cai de ~80 mA para menos de 10 µA.

Existem duas formas de acordar a placa:

| Fonte de wake-up | Configuração |
|------------------|-------------|
| **Botão SW1** (EXT0) | `esp32.wake_on_ext0(pin=sw1, level=WAKEUP_ALL_LOW)` |
| **Tempo esgotado** | `machine.deepsleep(TEMPO_MS)` — acorda após `TEMPO_MS` milissegundos |

Ao acordar, o ESP32 reinicia completamente e executa `boot.py` seguido de `main.py` novamente.

## Circuito

O botão SW1 já está integrado no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32. A placa exibirá uma mensagem, aguardará 1 segundo e entrará em deep sleep. Pressione SW1 ou aguarde o tempo configurado para acordá-la.

## Exemplo de Saída Serial

```
Entrando em deep sleep por 10 segundos.
Pressione SW1 (GPIO 18) para acordar antes.
[placa dorme — reinicia ao acordar]
Entrando em deep sleep por 10 segundos.
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 12** — Interrupções, temporizadores e threads › **Deep sleep** e **Sensor de presença**  
> Disponível na biblioteca para consulta presencial.
