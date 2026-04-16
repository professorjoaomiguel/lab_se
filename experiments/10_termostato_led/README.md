# Experimento 10 — Termostato com Indicador LED

## Objetivo

Ler a temperatura ambiente com o sensor LM35 e indicar visualmente o estado térmico: LED vermelho (D13) acende quando a temperatura ultrapassa o limiar; LED azul (D12) acende quando está abaixo.

## Componentes Utilizados

| Componente         | Pino GPIO       |
|--------------------|-----------------|
| LM35               | GPIO 1 (ADC)    |
| LED azul (D12)     | GPIO 12         |
| LED vermelho (D13) | GPIO 13         |

## Como Funciona

O LM35 gera **10 mV por °C**. O ADC lê a tensão e converte para temperatura:

```
tensão (V)       = leitura / 4095 × 3.3
temperatura (°C) = tensão / 0.01
```

A temperatura é comparada com `LIMIAR` (padrão: 30 °C):

| Condição               | Indicação visual |
|------------------------|------------------|
| Temperatura > LIMIAR   | D13 aceso (vermelho) — ALTA |
| Temperatura ≤ LIMIAR   | D12 aceso (azul) — OK       |

## Circuito

Todos os componentes já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32. Ajuste a constante `LIMIAR` conforme necessário. Abra o monitor serial para acompanhar as leituras.

## Exemplo de Saída Serial

```
Termostato pronto. Limiar: 30.0 °C
Temp: 27.80 °C | OK
Temp: 28.14 °C | OK
Temp: 30.52 °C | ALTA
Temp: 31.05 °C | ALTA
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Conversor analógico digital** e **Medidor de temperatura com termístor**  
> Disponível na biblioteca para consulta presencial.
