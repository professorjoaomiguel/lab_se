# Mapeamento de Pinos — ESP32 (Form Factor Arduino UNO)

A placa ESP32 utilizada nos experimentos possui o form factor do Arduino UNO.
A tabela abaixo relaciona os pinos do Shield com os GPIOs do ESP32.

---

## Pinos Digitais

| Pino Shield | GPIO ESP32 | Função nos Experimentos |
|-------------|-----------|------------------------|
| D4          | GPIO 4    | Sensor DHT11 (dados) |
| D5          | GPIO 5    | Buzzer (PWM) |
| D9          | GPIO 9    | LED RGB – Vermelho (PWM) |
| D10         | GPIO 10   | LED RGB – Verde (PWM) |
| D11         | GPIO 11   | LED RGB – Azul (PWM) |
| D12         | GPIO 12   | LED azul / LED D12     |
| D13         | GPIO 13   | LED vermelho / LED D13 (PWM) |
| D17         | GPIO 17   | Botão SW2 (Pull-Up interno) |
| D18         | GPIO 18   | Botão SW1 (Pull-Up interno) |

## Pinos Analógicos

| Pino Shield | GPIO ESP32 | Função nos Experimentos |
|-------------|-----------|------------------------|
| A0          | GPIO 36   | Potenciômetro |
| A1          | GPIO 1    | LDR (fotocélula) |
| A2          | GPIO 2    | Sensor LM35 |

---

## Notas Importantes

- Os botões SW1 e SW2 usam **Pull-Up interno** — o pino lê `0` quando o botão está pressionado.
- O ADC do ESP32 opera de **0 a 3,3 V** com resolução de **12 bits** (0–4095).
- Ao usar `ADC.ATTN_11DB` a faixa de leitura chega a ~3,3 V.
- Os pinos GPIO 1 e GPIO 3 têm uso especial na UART0 (console); verifique possíveis conflitos ao usar GPIO 1 como ADC.
- O PWM no MicroPython usa `duty()` com valores de **0 a 1023**.
- GPIO 11 está conectado ao barramento SPI da flash interna em alguns módulos ESP32; teste antes de usar.
- Para detalhes completos dos periféricos do shield, consulte [shield_9in1.md](shield_9in1.md).
