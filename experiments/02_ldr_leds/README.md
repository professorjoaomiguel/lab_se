# Experimento 2 — Fotocélula e LEDs

## Objetivo

Com a mescla da fotocélula (LDR) e dos LEDs, é possível saber se a intensidade de luz está na máxima ou não. Se estiver, o LED vermelho (D13) permanecerá aceso; caso contrário, o LED azul (D12) acenderá.

## Componentes Utilizados

| Componente    | Pino GPIO |
|---------------|-----------|
| LDR (fotocélula) | GPIO 1 (ADC) |
| LED azul (D12)   | GPIO 12 |
| LED vermelho (D13) | GPIO 13 |

## Como Funciona

O LDR é lido pelo ADC configurado com resolução de 12 bits (0–4095) e atenuação de 11 dB (~3,3 V de faixa). Quanto mais luz, maior o valor lido.

- Valor > 2000 → **LED vermelho (D13) aceso** — luz intensa
- Valor ≤ 2000 → **LED azul (D12) aceso** — luz fraca

## Circuito

Os componentes já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial para acompanhar os valores do LDR.

## Exemplo de Saída Serial

```
Luz: 3102
Luz: 3256
Luz: 1450
Luz: 980
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Conversor analógico digital** e **Medidor de intensidade luminosa**  
> Disponível na biblioteca para consulta presencial.
