# Documentação Técnica: ESP32 UNO (D1 R32)

Este documento descreve as especificações técnicas da placa principal utilizada nos experimentos, que integra um módulo **ESP-WROOM-32** em um formato físico compatível com **Arduino UNO (D1 R32)**.

---

## 🚀 Especificações Principais

- **Microcontrolador:** ESP-WROOM-32 (Xtensa® Dual-Core 32-bit LX6).
- **Clock:** Ajustável de 80 MHz a 240 MHz.
- **Memória Flash:** 4 MB.
- **SRAM:** 520 KB.
- **Conectividade:** 
  - Wi-Fi 802.11 b/g/n (até 150 Mbps).
  - Bluetooth v4.2 BR/EDR e BLE (Dual Mode).
- **Conversor USB-Serial:** Geralmente CH340 ou CP2102.
- **Form Factor:** Arduino UNO R3 compatible.

---

## ⚡ Parâmetros Elétricos

- **Tensão de Operação (Lógica):** 3.3V. 
  - *Atenção:* Os pinos de entrada **não são tolerantes a 5V**. O Shield 9-em-1 já está adaptado para isso.
- **Tensão de Entrada (Vin / DC Jack):** 5V a 12V DC.
- **Corrente por GPIO:** 12 mA (recomendado), 20 mA (máximo).

---

## 📍 Mapeamento e Recursos de Hardware

A placa mapeia os GPIOs do ESP32 para os conectores no padrão Arduino.

### Periféricos Internos
- **ADC (Conversor Analógico-Digital):** 12 bits de resolução. Usado nos pinos A0 a A5.
- **DAC (Conversor Digital-Analógico):** 8 bits. Disponível em pinos específicos.
- **PWM:** Disponível em quase todos os pinos digitais (D0-D13).
- **UART:** 3 interfaces (UART0 usada para o terminal via USB).
- **I2C / SPI:** Barramentos de comunicação serial para sensores externos.

---

## 🔗 Referências Oficiais
- **Modelo de Referência (Loja):** [TZT ESP32-Uno D1 R3](https://www.tztstore.com/goods/show-6284.html)
- **Documentação do MicroPython (ESP32):** [docs.micropython.org](https://docs.micropython.org/en/latest/esp32/quickref.html)
- **Datasheet do Módulo ESP-WROOM-32:** [Espressif Systems](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf)

---

## ⚠️ Observação Pedagógica
Diferente do Arduino UNO clássico (que opera em 5V), o ESP32 trabalha em **3.3V**. Sempre verifique o datasheet de novos componentes antes de ligá-los diretamente aos pinos para evitar danos permanentes ao microcontrolador.
