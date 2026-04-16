# Experimento 6 — Dimer com Potenciômetro

## Objetivo

Utilizar o potenciômetro para controlar (dimerizar) a intensidade luminosa do LED RGB via leitura analógica.

## Componentes Utilizados

| Componente      | Pino GPIO |
|-----------------|-----------|
| Potenciômetro   | GPIO 2 (ADC) |

## Como Funciona

O potenciômetro é lido pelo ADC (0–4095, 12 bits, faixa até ~3,3 V com `ATTN_11DB`). O valor bruto é convertido para percentual (0–100%) e exibido no monitor serial.

Para controlar o brilho de um LED com PWM, o valor lido (0–4095) pode ser mapeado para a escala do `duty()` (0–1023):

```python
duty = int((valor / 4095) * 1023)
led_pwm.duty(duty)
```

## Circuito

O potenciômetro já está integrado no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial para acompanhar os valores lidos.

## Exemplo de Saída Serial

```
Lendo potenciômetro no GPIO 2
Bruto: 0   |  0 %
Bruto: 2048  |  50 %
Bruto: 4095  |  100 %
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 3** — Portas de entrada e saída › **Conversor analógico digital**  
> Disponível na biblioteca para consulta presencial.
