# Experimento 3 — LED RGB com LDR e PWM

## Objetivo

Se o ambiente estiver com luz forte, o LED vermelho acenderá; caso contrário, o LED verde do RGB ficará aceso. A intensidade dos LEDs é controlada proporcionalmente via PWM.

## Componentes Utilizados

| Componente       | Pino GPIO |
|------------------|-----------|
| LDR (fotocélula) | GPIO 1 (ADC) |
| LED verde (RGB)  | GPIO 10 (PWM) |
| LED vermelho (RGB) | GPIO 13 (PWM) |

## Como Funciona

O LDR é lido pelo ADC (0–4095). A leitura é dividida em três faixas:

| Faixa de Leitura | Comportamento |
|------------------|---------------|
| < 1200           | LED **verde** acende com brilho proporcional (pouca luz) |
| 1200 – 2600      | LED **verde** acende com brilho proporcional (transição) |
| > 2600           | LED **vermelho** acende com brilho proporcional (luz forte) |

O PWM usa `duty()` com valores de 0 a 1023.

## Circuito

Os componentes já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial para acompanhar os valores do LDR.

## Exemplo de Saída Serial

```
LDR: 850
LDR: 1650
LDR: 3100
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Modulação por largura de pulso (PWM)**, **LED RGB** e **Medidor de intensidade luminosa**  
> Disponível na biblioteca para consulta presencial.
