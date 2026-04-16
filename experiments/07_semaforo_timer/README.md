# Experimento 7 — Semáforo com Temporização

## Objetivo

Simular um semáforo usando os LEDs D12 (representa verde) e D13 (vermelho) do Shield com temporização precisa via `machine.Timer`, eliminando bloqueios causados por `sleep()`.

> **Nota:** O LED D12 é fisicamente azul no Shield. Neste experimento ele representa a fase verde do semáforo.

## Componentes Utilizados

| Componente          | Pino GPIO |
|---------------------|-----------|
| LED D12 (verde no semáforo) | GPIO 12  |
| LED vermelho (D13)  | GPIO 13   |

## Como Funciona

O programa define três fases cíclicas do semáforo, cada uma com duração diferente:

| Fase | D12 | D13 | Duração |
|------|-----|-----|---------|
| 0 — Verde    | Aceso  | Apagado | 4000 ms |
| 1 — Amarelo  | Apagado| Apagado | 1000 ms |
| 2 — Vermelho | Apagado| Aceso   | 3000 ms |

Um `Timer` em modo `ONE_SHOT` é reiniciado ao final de cada fase com o período da fase seguinte. A função `proxima_fase()` é o callback do timer: atualiza os LEDs, avança o índice da fase e reprograma o timer para a duração correta.

## Circuito

Os LEDs já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial para acompanhar as transições de fase.

## Exemplo de Saída Serial

```
Fase: 0 | D12: 1 | D13: 0
Fase: 1 | D12: 0 | D13: 0
Fase: 2 | D12: 0 | D13: 1
Fase: 0 | D12: 1 | D13: 0
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Simulação de um semáforo**  
> **Capítulo 12** — Interrupções, temporizadores e threads › **Temporizadores**  
> Disponível na biblioteca para consulta presencial.
