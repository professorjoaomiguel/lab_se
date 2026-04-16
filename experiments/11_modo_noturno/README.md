# Experimento 11 — Modo Noturno Automático

## Objetivo

Controlar o brilho do LED verde do RGB de forma inversamente proporcional à luminosidade ambiente lida pelo LDR — quanto menos luz no ambiente, mais brilhante o LED (comportamento de iluminação noturna automática).

## Componentes Utilizados

| Componente         | Pino GPIO        |
|--------------------|------------------|
| LDR (fotocélula)   | GPIO 1 (ADC)     |
| LED verde (RGB)    | GPIO 10 (PWM)    |

## Como Funciona

O LDR é lido pelo ADC (0 = escuro, 4095 = muito iluminado). O brilho do LED é calculado com a **relação inversa**:

```
brilho = int((1 - valor / 4095) * 1023)
```

| Luminosidade | Valor LDR | Brilho LED |
|--------------|-----------|------------|
| Escuro       | ≈ 0       | ≈ 1023 (máximo) |
| Meia luz     | ≈ 2048    | ≈ 511 (médio)   |
| Luz forte    | ≈ 4095    | ≈ 0 (apagado)   |

O resultado é aplicado ao LED via `PWM.duty()`.

## Circuito

Todos os componentes já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32. Cubra ou ilumine o LDR e observe o LED verde alterar o brilho automaticamente.

## Exemplo de Saída Serial

```
Modo noturno pronto. Cubra o LDR para aumentar o brilho.
LDR: 3200 | Brilho: 221
LDR: 1500 | Brilho: 649
LDR: 200  | Brilho: 972
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Medidor de intensidade luminosa** e **Modulação por largura de pulso (PWM)**  
> Disponível na biblioteca para consulta presencial.
