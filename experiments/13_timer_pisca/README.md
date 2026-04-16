# Experimento 13 — Pisca-pisca com Timer (sem sleep)

## Objetivo

Redesenhar o Exp. 04 (pisca-pisca) usando `machine.Timer` para alternar os LEDs em intervalos precisos **sem bloquear a CPU**, demonstrando como liberar o loop principal para outras tarefas simultâneas.

## Componentes Utilizados

| Componente         | Pino GPIO |
|--------------------|-----------|
| LED azul (D12)     | GPIO 12   |
| LED vermelho (D13) | GPIO 13   |

## Como Funciona

Um `Timer` configurado em modo `PERIODIC` dispara o callback `alternar()` a cada 500 ms. O callback inverte um flag de estado e aplica os valores aos dois LEDs:

```
D12 = estado
D13 = not estado
```

O loop principal (`while True: pass`) fica completamente livre — não há nenhuma chamada a `sleep()`. Em uma aplicação real, este loop poderia ler sensores, processar dados ou comunicar via rede enquanto os LEDs piscam.

## Circuito

Os LEDs já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32. Os LEDs começarão a piscar automaticamente e o terminal exibirá a mensagem do loop principal.

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 12** — Interrupções, temporizadores e threads › **Temporizadores**  
> Disponível na biblioteca para consulta presencial.
