# Experimento 5 — Sensor de Temperatura LM35

## Objetivo

Utilizar o sensor LM35 para medir a temperatura do ambiente e exibir o valor em graus Celsius no monitor serial.

## Componentes Utilizados

| Componente | Pino GPIO |
|------------|-----------|
| LM35       | GPIO 1 (ADC) |

## Como Funciona

O LM35 gera uma tensão de saída proporcional à temperatura: **10 mV por °C**.

O ADC do ESP32 lê a tensão do sensor (0–3,3 V, resolução 12 bits = 0–4095) e converte para temperatura:

```
tensão (V) = leitura / 4095 × 3,3
temperatura (°C) = tensão / 0,01   (10 mV/°C = 0,01 V/°C)
```

A leitura é atualizada a cada 1 segundo.

## Circuito

O sensor LM35 já está integrado no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial para acompanhar as leituras de temperatura.

## Exemplo de Saída Serial

```
Temperatura: 27.45 °C
Temperatura: 27.52 °C
Temperatura: 28.01 °C
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Conversor analógico digital** e **Medidor de temperatura com termístor**  
> Disponível na biblioteca para consulta presencial.
