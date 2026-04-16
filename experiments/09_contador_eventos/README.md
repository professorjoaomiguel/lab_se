# Experimento 9 — Contador de Eventos

## Objetivo

Contar quantas vezes cada botão do Shield foi pressionado e exibir os contadores no monitor serial. Pressionar SW1 e SW2 simultaneamente zera ambos os contadores.

## Componentes Utilizados

| Componente | Pino GPIO |
|------------|-----------|
| Botão SW1  | GPIO 18   |
| Botão SW2  | GPIO 17   |

## Como Funciona

O código lê os estados de SW1 e SW2 em cada iteração do loop:

| Condição               | Ação                        |
|------------------------|-----------------------------|
| SW1 e SW2 pressionados | Zera `cont_sw1` e `cont_sw2` |
| Só SW1 pressionado     | Incrementa `cont_sw1`        |
| Só SW2 pressionado     | Incrementa `cont_sw2`        |

Um `sleep(0.2)` após cada evento garante o debounce. A prioridade do reset (ambos ao mesmo tempo) é verificada primeiro na estrutura `if/elif`.

## Circuito

Os botões já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial para acompanhar os contadores.

## Exemplo de Saída Serial

```
Contador pronto. SW1 e SW2 incrementam. SW1+SW2 zera.
SW1: 1 | SW2: 0
SW1: 2 | SW2: 0
SW1: 2 | SW2: 1
Contadores zerados!
SW1: 1 | SW2: 0
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 2** — Introdução ao Python › **Variáveis e operadores** e **Seleção e repetição**  
> **Capítulo 3** — Portas de entrada e saída › **Entrada digital**  
> Disponível na biblioteca para consulta presencial.
