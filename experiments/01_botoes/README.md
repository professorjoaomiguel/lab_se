# Experimento 1 — Botões

## Objetivo

Reconhecer qual botão foi pressionado no Shield, identificando SW1 (GPIO 18) e SW2 (GPIO 17).

## Componentes Utilizados

| Componente | Pino GPIO |
|------------|-----------|
| Botão SW1  | GPIO 18   |
| Botão SW2  | GPIO 17   |

## Como Funciona

Ambos os botões são configurados com **Pull-Up interno**. Isso significa que o pino lê `1` (alto) quando o botão está solto e `0` (baixo) quando pressionado.

O código verifica continuamente o estado dos dois botões e imprime uma mensagem no console serial sempre que um deles é acionado. Um pequeno atraso de debounce (200 ms) evita leituras duplicadas por trepidação mecânica do botão.

## Circuito

Não é necessária nenhuma ligação externa — os botões já estão integrados no Shield.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial para ver as mensagens.

## Exemplo de Saída Serial

```
Botões prontos...
SW1 pressionado
SW2 pressionado
SW1 pressionado
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Entrada digital**  
> Disponível na biblioteca para consulta presencial.
