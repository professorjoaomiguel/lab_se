# Experimento 12 — Interrupções por Botão (IRQ)

## Objetivo

Reagir ao pressionamento de SW1 e SW2 usando **interrupções de hardware** (`Pin.irq()`), sem bloquear o loop principal com polling. Este é um conceito fundamental em sistemas embarcados: o processador é notificado pelo hardware apenas quando o evento ocorre.

## Componentes Utilizados

| Componente | Pino GPIO |
|------------|-----------|
| Botão SW1  | GPIO 18   |
| Botão SW2  | GPIO 17   |

## Como Funciona

Cada botão tem uma **IRQ registrada na borda de descida** (`IRQ_FALLING`): quando o pino vai de HIGH para LOW (botão pressionado), o MicroPython chama automaticamente o callback correspondente, independentemente do que o loop principal esteja fazendo.

| Evento              | Callback   | Ação                        |
|---------------------|------------|-----------------------------|
| SW1 pressionado     | `cb_sw1()` | Incrementa `cont_sw1`       |
| SW2 pressionado     | `cb_sw2()` | Incrementa `cont_sw2`       |
| Loop principal (1 s)| —          | Imprime contadores no serial |

O loop principal fica completamente livre para outras tarefas enquanto as interrupções respondem aos botões em tempo real.

## Circuito

Os botões já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial. Pressione os botões e observe que o callback é disparado imediatamente.

## Exemplo de Saída Serial

```
IRQ configurado. Pressione SW1 ou SW2.
SW1 pressionado! Total SW1: 1
SW2 pressionado! Total SW2: 1
Loop principal em execução... SW1: 1 SW2: 1
SW1 pressionado! Total SW1: 2
Loop principal em execução... SW1: 2 SW2: 1
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 12** — Interrupções, temporizadores e threads › **Interrupções**  
> Disponível na biblioteca para consulta presencial.
