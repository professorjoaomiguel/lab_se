# Experimento 4 — Pisca-pisca com LEDs

## Objetivo

Piscar alternadamente os LEDs presentes no Shield, servindo como introdução ao controle de saídas digitais com MicroPython.

## Componentes Utilizados

| Componente     | Pino GPIO |
|----------------|-----------|
| LED azul (D12) | GPIO 12   |
| LED vermelho (D13) | GPIO 13 |

## Como Funciona

O código liga D12 e apaga D13 por 500 ms, depois inverte o estado — apaga D12 e liga D13 por mais 500 ms — repetindo o ciclo indefinidamente.

## Circuito

Os LEDs já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32. Os LEDs começarão a piscar imediatamente após a inicialização.

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Saída digital** e **Simulação de um semáforo**  
> Disponível na biblioteca para consulta presencial.
