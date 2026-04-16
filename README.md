# Lab SE — Laboratório de Sistemas Embarcados

Repositório base para experimentos práticos da disciplina de **Sistemas Embarcados**.

## 🔧 Plataforma

- **Hardware:** Placa ESP32 com form factor Arduino UNO + Shield de experimentos
- **Linguagem:** [MicroPython](https://micropython.org/)

## 📁 Estrutura do Repositório

```
lab_se/
├── docs/                         # Documentação e guias de referência
│   ├── setup.md                  # Guia de instalação do ambiente
│   └── esp32_pinout.md           # Mapeamento de pinos do ESP32
├── experiments/                  # Experimentos práticos
│   ├── 01_botoes/                # Exp. 01 – Leitura de botões
│   ├── 02_ldr_leds/              # Exp. 02 – Fotocélula e LEDs
│   ├── 03_rgb_ldr/               # Exp. 03 – LED RGB com LDR e PWM
│   ├── 04_pisca_pisca/           # Exp. 04 – Pisca-pisca com LEDs
│   ├── 05_lm35/                  # Exp. 05 – Sensor de temperatura LM35
│   └── 06_potenciometro/         # Exp. 06 – Dimer com potenciômetro
└── lib/                          # Bibliotecas e utilitários comuns
    └── utils.py
```

## 🚀 Como Começar

1. Leia o [Guia de Instalação](docs/setup.md) para preparar o ambiente.
2. Consulte o [Mapeamento de Pinos](docs/esp32_pinout.md) antes de montar os circuitos.
3. Acesse a pasta do experimento desejado em `experiments/` e siga as instruções do `README.md` local.

## 📋 Lista de Experimentos

| # | Experimento | Descrição |
|---|-------------|-----------|
| 01 | [Botões](experiments/01_botoes/) | Reconhecer qual botão do Shield foi pressionado |
| 02 | [Fotocélula e LEDs](experiments/02_ldr_leds/) | LED vermelho na luz máxima, azul caso contrário |
| 03 | [LED RGB com LDR](experiments/03_rgb_ldr/) | LED vermelho em luz forte, verde caso contrário |
| 04 | [Pisca-pisca](experiments/04_pisca_pisca/) | Piscar alternadamente os LEDs do Shield |
| 05 | [Sensor LM35](experiments/05_lm35/) | Medir temperatura ambiente com o LM35 |
| 06 | [Potenciômetro](experiments/06_potenciometro/) | Dimerizaçāo do LED RGB com potenciômetro |

## 📚 Recursos Úteis

- [Documentação oficial do MicroPython](https://docs.micropython.org/)
- [Firmware MicroPython para ESP32](https://micropython.org/download/ESP32_GENERIC/)
- [Thonny IDE](https://thonny.org/) — IDE recomendada para iniciantes
- [esptool](https://github.com/espressif/esptool) — Ferramenta para gravar firmware

## 📝 Licença

Este repositório é disponibilizado para fins educacionais.


Repositório base para experimentos práticos da disciplina de **Sistemas Embarcados**.

## 🔧 Plataforma

- **Hardware:** Placa ESP32 com form factor Arduino UNO
- **Linguagem:** [MicroPython](https://micropython.org/)

## 📁 Estrutura do Repositório

```
lab_se/
├── docs/                   # Documentação e guias de referência
│   ├── setup.md            # Guia de instalação do ambiente
│   └── esp32_pinout.md     # Mapeamento de pinos do ESP32
├── experiments/            # Experimentos práticos
│   ├── 01_blink/           # Exp. 01 – Pisca LED (Hello World)
│   ├── 02_button/          # Exp. 02 – Leitura de botão (entrada digital)
│   ├── 03_pwm/             # Exp. 03 – PWM e controle de brilho
│   ├── 04_adc/             # Exp. 04 – Leitura analógica (ADC)
│   ├── 05_i2c/             # Exp. 05 – Comunicação I2C
│   └── 06_uart/            # Exp. 06 – Comunicação UART
└── lib/                    # Bibliotecas e utilitários comuns
    └── utils.py
```

## 🚀 Como Começar

1. Leia o [Guia de Instalação](docs/setup.md) para preparar o ambiente.
2. Consulte o [Mapeamento de Pinos](docs/esp32_pinout.md) antes de montar os circuitos.
3. Acesse a pasta do experimento desejado em `experiments/` e siga as instruções do `README.md` local.

## 📋 Lista de Experimentos

| # | Experimento | Descrição |
|---|-------------|-----------|
| 01 | [Blink](experiments/01_blink/) | Piscar um LED – introdução ao MicroPython no ESP32 |
| 02 | [Button](experiments/02_button/) | Ler o estado de um botão (entrada digital) |
| 03 | [PWM](experiments/03_pwm/) | Controlar o brilho de um LED com PWM |
| 04 | [ADC](experiments/04_adc/) | Ler um sensor analógico (potenciômetro) |
| 05 | [I2C](experiments/05_i2c/) | Comunicar com dispositivo via barramento I2C |
| 06 | [UART](experiments/06_uart/) | Comunicação serial via UART |

## 📚 Recursos Úteis

- [Documentação oficial do MicroPython](https://docs.micropython.org/)
- [Firmware MicroPython para ESP32](https://micropython.org/download/ESP32_GENERIC/)
- [Ferramenta Thonny IDE](https://thonny.org/)
- [Ferramenta ampy (upload de arquivos)](https://github.com/scientifichackers/ampy)
- [Ferramenta rshell](https://github.com/dhylands/rshell)

## 📝 Licença

Este repositório é disponibilizado para fins educacionais.
