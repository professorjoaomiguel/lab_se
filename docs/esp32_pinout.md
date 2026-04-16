# Mapeamento de Pinos — ESP32 (Form Factor Arduino UNO)

A placa ESP32 utilizada nos experimentos possui o form factor do Arduino UNO.
A tabela abaixo relaciona os pinos do Shield com os GPIOs do ESP32.

---

## Pinos Digitais

| Pino Shield | GPIO ESP32 | Função nos Experimentos |
|-------------|-----------|------------------------|
| D10         | GPIO 10   | LED verde do RGB (PWM) |
| D12         | GPIO 12   | LED azul / LED D12     |
| D13         | GPIO 13   | LED vermelho / LED D13 (PWM) |
| D17         | GPIO 17   | Botão SW2 (Pull-Up interno) |
| D18         | GPIO 18   | Botão SW1 (Pull-Up interno) |

## Pinos Analógicos

| Pino Shield | GPIO ESP32 | Função nos Experimentos |
|-------------|-----------|------------------------|
| A1          | GPIO 1    | LDR (fotocélula) / LM35 |
| A2          | GPIO 2    | Potenciômetro |

---

## Notas Importantes

- Os botões SW1 e SW2 usam **Pull-Up interno** — o pino lê `0` quando o botão está pressionado.
- O ADC do ESP32 opera de **0 a 3,3 V** com resolução de **12 bits** (0–4095).
- Ao usar `ADC.ATTN_11DB` a faixa de leitura chega a ~3,3 V.
- Os pinos GPIO 1 e GPIO 3 têm uso especial na UART0 (console); verifique possíveis conflitos ao usar GPIO 1 como ADC.
- O PWM no MicroPython usa `duty()` com valores de **0 a 1023**.
