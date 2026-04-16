# Experimento 8 — Dimmer por Botões

## Objetivo

Controlar o brilho do LED verde do RGB via PWM usando os botões do Shield: SW1 aumenta o brilho e SW2 diminui, combinando entrada digital com saída PWM.

## Componentes Utilizados

| Componente         | Pino GPIO        |
|--------------------|------------------|
| Botão SW1          | GPIO 18          |
| Botão SW2          | GPIO 17          |
| LED verde (RGB)    | GPIO 10 (PWM)    |

## Como Funciona

O LED verde é controlado por PWM com valores de `duty` de 0 (apagado) a 1023 (brilho máximo). A cada pressionamento:

- **SW1** → incrementa o brilho em 64 (limitado a 1023)
- **SW2** → decrementa o brilho em 64 (limitado a 0)

Um `sleep(0.2)` após cada detecção implementa o debounce por software, evitando múltiplos incrementos por um único pressionamento.

## Circuito

Todos os componentes já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e observe o LED verde mudar de brilho ao pressionar os botões.

## Exemplo de Saída Serial

```
Dimmer pronto. SW1 aumenta, SW2 diminui.
Brilho inicial: 512
Brilho: 576
Brilho: 640
Brilho: 576
Brilho: 512
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Entrada digital** e **Modulação por largura de pulso (PWM)**  
> Disponível na biblioteca para consulta presencial.
