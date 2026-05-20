# Shield 9-em-1 — Placa de Expansão com Periféricos

> **Fonte:** [RoboticXps/nine-in-one-expansion-sensor-board-arduino](https://github.com/RoboticXps/nine-in-one-expansion-sensor-board-arduino)  
> **Loja:** [roboticx.ps](https://roboticx.ps/)  
> **Canal YouTube:** [@Roboticxps](https://www.youtube.com/@Roboticxps)

---

## Visão Geral

O **Shield 9-em-1** (9-in-1 Multifunctional Expansion Board) é um shield no form factor do Arduino UNO que integra nove componentes eletrônicos na mesma placa.

Neste laboratório, o shield é encaixado sobre uma placa **ESP32 UNO** (disponível em [tztstore.com](https://www.tztstore.com/goods/show-6284.html)) e programado em **MicroPython**.

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

Os experimentos foram organizados em uma trilha pedagógica de complexidade crescente, cobrindo todos os periféricos do shield multifuncional:

| Experimento | Componente do Shield | Link |
|-------------|----------------------|------|
| [01 – Pisca-pisca com LEDs](../experiments/01_pisca_pisca/) | LED Azul (D12) e LED Vermelho (D13) | GPIO 12 / GPIO 13 |
| [02 – Botões e Interação](../experiments/02_botoes/) | Botões SW1 e SW2 + LED Azul | GPIO 18 / GPIO 17 / GPIO 12 |
| [03 – Fotocélula (LDR) e Histerese](../experiments/03_ldr_leds/) | LDR (fotocélula) + LED Vermelho | GPIO 1 / GPIO 13 |
| [04 – LED RGB e PWM](../experiments/04_rgb_ldr/) | LED RGB Verde e Vermelho + LDR | GPIO 10 / GPIO 9 / GPIO 1 |
| [05 – Sensor de Temperatura LM35](../experiments/05_lm35/) | Sensor LM35 | GPIO 2 |
| [06 – Dimer com Potenciômetro](../experiments/06_potenciometro/) | Potenciômetro + LED Azul (PWM) | GPIO 36 / GPIO 12 |
| [07 – Buzzer e Frequência](../experiments/07_buzzer/) | Buzzer Piezoelétrico + Botões | GPIO 5 / GPIO 18, 17 |
| [08 – Sensor DHT11](../experiments/08_dht11/) | Sensor DHT11 + LED Vermelho | GPIO 4 / GPIO 13 |
| [09 – Wi-Fi e Servidor Web (IoT)](../experiments/09_wifi/) | Wi-Fi + Potenciômetro | Chip interno / GPIO 36 |

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

## 🎯 Cobertura Total de Periféricos

Com a reestruturação pedagógica recente, **100% dos periféricos do Shield 9-em-1** encontram-se cobertos por experimentos práticos em MicroPython neste repositório. Isso garante uma experiência completa de IoT e Sistemas Embarcados para os estudantes, avançando desde entradas e saídas básicas até conectividade de rede e monitoramento web em tempo real.
