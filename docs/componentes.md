# Documentação Técnica dos Componentes

Esta seção fornece os detalhes técnicos dos componentes integrados no **Shield 9-em-1**. É fundamental que o aluno consulte estas informações para configurar corretamente os ganhos e escalas no código.

---

## 🌡️ Sensor de Temperatura LM35
O LM35 é um sensor de precisão que fornece uma tensão de saída linearmente proporcional à temperatura em Celsius.

- **Fator de Escala:** 10 mV / °C (Ex: 250 mV = 25 °C).
- **Faixa de Tensão:** Opera de 4V a 30V. No shield, é alimentado por 5V ou 3.3V.
- **Precisão:** ±0,5 °C em temperatura ambiente.
- **Desafio Pedagógico:** Como o ESP32 lê até 3.3V (com atenuação de 11dB), o LM35 nunca atingirá o limite do ADC (pois 150 °C seriam 1.5V). Verifique se a resolução de 12 bits é suficiente para detectar variações de 0.1 °C.
- **[Download Datasheet (TI)](https://www.ti.com/lit/ds/symlink/lm35.pdf)**

---

## 💧 Sensor de Temperatura e Umidade DHT11
Sensor digital que utiliza um protocolo de fio único (1-wire) para enviar dados.

- **Faixa de Umidade:** 20-90% RH (±5%).
- **Faixa de Temperatura:** 0-50 °C (±2%).
- **Interface:** Digital (Não utiliza o ADC).
- **[Download Datasheet (Adafruit)](https://www.mouser.com/datasheet/2/758/DHT11-934525.pdf)**

---

## 🔆 Fotocélula (LDR)
Resistor dependente de luz. Sua resistência diminui conforme a intensidade luminosa aumenta.

- **Tipo:** CdS (Sulfeto de Cádmio) 5mm.
- **Comportamento:** Atua em um divisor de tensão no shield.
- **Atenção:** Verifique no esquema do shield se o LDR está conectado ao VCC ou ao GND para entender se a leitura do ADC sobe ou desce com a luz.

---

## 🎨 LED RGB (Anodo Comum ou Catodo Comum)
O shield utiliza um LED RGB que combina as cores Vermelho (Red), Verde (Green) e Azul (Blue).

- **Tensão de Operação (Vf):** 
  - Vermelho: ~2.0V
  - Verde/Azul: ~3.2V
- **Controle:** Deve ser usado com PWM (`machine.PWM`) para misturar cores.

---

## 🔘 Botões e LEDs Discretos
- **Botões:** Chaves táteis. No ESP32, utilize `Pin.PULL_UP` para garantir o estado logico `1` quando soltos.
- **LEDs (D12/D13):** LEDs comuns de 5mm. D13 no shield costuma estar em série com um resistor de 220-330 Ohms.

---

## ⚡ Conversor AD do ESP32 (Informação Crítica)
O aluno deve entender como o ESP32 interpreta sinais analógicos.

- **Resolução:** 12 bits (0 a 4095).
- **Atenuação e Faixas (Aprox.):**
  - `ADC.ATTN_0DB`: 0.0V — 1.0V
  - `ADC.ATTN_2_5DB`: 0.0V — 1.34V
  - `ADC.ATTN_6DB`: 0.0V — 2.0V
  - **`ADC.ATTN_11DB`**: 0.0V — 3.3V (Padrão para a maioria dos shields).

> **Exercício:** Se o LM35 produz no máximo 1.5V, qual seria a melhor atenuação para obter a maior precisão possível sem saturar o sensor?
