# Shield 9-em-1 — Placa de Expansão com Periféricos

> **Fonte:** [RoboticXps/nine-in-one-expansion-sensor-board-arduino](https://github.com/RoboticXps/nine-in-one-expansion-sensor-board-arduino)  
> **Loja:** [roboticx.ps](https://roboticx.ps/)  
> **Canal YouTube:** [@Roboticxps](https://www.youtube.com/@Roboticxps)

---

## Visão Geral

O **Shield 9-em-1** (9-in-1 Multifunctional Expansion Board) é um shield no form factor do Arduino UNO que integra nove componentes eletrônicos na mesma placa, eliminando a necessidade de protoboard e fios para os experimentos mais comuns.

Neste laboratório o shield é encaixado sobre um ESP32 com form factor Arduino UNO e programado em **MicroPython**.

---

## Componentes da Placa

| # | Componente | Descrição |
|---|-----------|-----------|
| 1 | **LED Vermelho** | LED discreto conectado ao pino D13 |
| 2 | **LED Azul** | LED discreto conectado ao pino D12 |
| 3 | **LED RGB** | LED tricolor (R/G/B) com pinos independentes D9/D10/D11 |
| 4 | **LDR** | Fotocélula (sensor de luminosidade) no pino A1 |
| 5 | **Potenciômetro** | Resistor variável rotativo no pino A0 |
| 6 | **Botão SW1** | Chave tátil no pino D18 (Pull-Up interno) |
| 7 | **Botão SW2** | Chave tátil no pino D17 (Pull-Up interno) |
| 8 | **Sensor DHT11** | Sensor de temperatura e umidade no pino D4 |
| 9 | **Sensor LM35** | Sensor de temperatura analógico no pino A2 |
| + | **Buzzer** | Buzzer piezoelétrico no pino D5 |

---

## Mapeamento de Pinos

A tabela abaixo relaciona o pino do shield (numeração Arduino) com o GPIO correspondente no ESP32 e o componente conectado.

### Pinos Digitais

| Pino Shield (Arduino) | GPIO ESP32 | Componente | Observações |
|-----------------------|-----------|------------|-------------|
| D4                    | GPIO 4    | DHT11      | Dados de temperatura e umidade |
| D5                    | GPIO 5    | Buzzer     | Saída PWM para geração de tom |
| D9                    | GPIO 9    | RGB – Vermelho | PWM disponível |
| D10                   | GPIO 10   | RGB – Verde    | PWM disponível |
| D11                   | GPIO 11   | RGB – Azul     | PWM disponível |
| D12                   | GPIO 12   | LED Azul   | Saída digital |
| D13                   | GPIO 13   | LED Vermelho | Saída digital / PWM |
| D17                   | GPIO 17   | Botão SW2  | Pull-Up interno; lê `0` ao pressionar |
| D18                   | GPIO 18   | Botão SW1  | Pull-Up interno; lê `0` ao pressionar |

### Pinos Analógicos

| Pino Shield (Arduino) | GPIO ESP32 | Componente | Observações |
|-----------------------|-----------|------------|-------------|
| A0                    | GPIO 36   | Potenciômetro | ADC 12 bits (0–4095) |
| A1                    | GPIO 1    | LDR (fotocélula) | Ver nota sobre conflito UART |
| A2                    | GPIO 2    | Sensor LM35 | 10 mV/°C |

> ⚠️ **Nota:** GPIO 1 é também o pino TX da UART0 (console serial). Ao usar o LDR como ADC, certifique-se de que o console serial não está ativo simultaneamente.

---

## Experimentos Disponíveis neste Repositório

| Experimento | Componente do Shield | Link |
|-------------|----------------------|------|
| [01 – Botões](../experiments/01_botoes/) | Botões SW1 e SW2 | GPIO 18 / GPIO 17 |
| [02 – Fotocélula e LEDs](../experiments/02_ldr_leds/) | LDR + LEDs | GPIO 1 / GPIO 12,13 |
| [03 – LED RGB com LDR](../experiments/03_rgb_ldr/) | RGB + LDR | GPIO 9,10,11 / GPIO 1 |
| [04 – Pisca-pisca](../experiments/04_pisca_pisca/) | LEDs | GPIO 12, 13 |
| [05 – Sensor LM35](../experiments/05_lm35/) | Sensor LM35 | GPIO 2 |
| [06 – Potenciômetro](../experiments/06_potenciometro/) | Potenciômetro | GPIO 36 |

---

## Exemplos de Referência (Arduino / C++)

O repositório original contém exemplos em Arduino C++ que podem servir de referência para entender o funcionamento dos periféricos antes de traduzir a lógica para MicroPython.

| Exemplo Arduino | Periférico | Link |
|----------------|-----------|------|
| `buzzer-potentiometer/buzzer-potentionmeter1.ino` | Buzzer + Potenciômetro | [ver no GitHub](https://github.com/RoboticXps/nine-in-one-expansion-sensor-board-arduino/blob/main/buzzer-potentiometer/buzzer-potentionmeter1.ino) |
| `dht11/dht11-example.ino` | Sensor DHT11 | [ver no GitHub](https://github.com/RoboticXps/nine-in-one-expansion-sensor-board-arduino/blob/main/dht11/dht11-example.ino) |
| `ldr-led/ldr-led1.ino` | LDR + LED | [ver no GitHub](https://github.com/RoboticXps/nine-in-one-expansion-sensor-board-arduino/blob/main/ldr-led/ldr-led1.ino) |
| `rgb-led/rgb1.ino` | LED RGB | [ver no GitHub](https://github.com/RoboticXps/nine-in-one-expansion-sensor-board-arduino/blob/main/rgb-led/rgb1.ino) |
| `switch-led/switch-led.ino` | Botão + LED | [ver no GitHub](https://github.com/RoboticXps/nine-in-one-expansion-sensor-board-arduino/blob/main/switch-led/switch-led.ino) |
| `temp-lm35/tempLM35.ino` | Sensor LM35 | [ver no GitHub](https://github.com/RoboticXps/nine-in-one-expansion-sensor-board-arduino/blob/main/temp-lm35/tempLM35.ino) |

---

## Periféricos Ainda Não Cobertos pelos Experimentos

Os seguintes componentes do shield ainda não possuem experimento dedicado neste repositório e podem ser explorados como atividade de extensão:

| Componente | GPIO ESP32 | Sugestão de Experimento |
|-----------|-----------|------------------------|
| **Buzzer** | GPIO 5 | Gerar tons musicais variando frequência com `PWM` |
| **DHT11** | GPIO 4 | Medir temperatura e umidade usando a biblioteca `dht` do MicroPython |

### Biblioteca DHT no MicroPython

O MicroPython inclui suporte nativo ao DHT11:

```python
import dht
from machine import Pin

sensor = dht.DHT11(Pin(4))
sensor.measure()
print("Temperatura:", sensor.temperature(), "°C")
print("Umidade:    ", sensor.humidity(), "%")
```

### Buzzer com PWM no MicroPython

```python
from machine import Pin, PWM
import time

buzzer = PWM(Pin(5), freq=440, duty=512)  # Lá (440 Hz)
time.sleep(1)
buzzer.deinit()  # Desliga o buzzer
```
