# Guia de Instalação do Ambiente

Este guia descreve os passos para configurar o ambiente de desenvolvimento para programar o ESP32 com MicroPython.

> 📖 **Referência:** *IoT com MicroPython e NodeMCU* — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 1** — NodeMCU e MicroPython › Programas utilizados · Atualização do firmware  
> Disponível na biblioteca para consulta presencial.

---

## 1. Pré-requisitos

- Python 3.x instalado no computador ([python.org](https://www.python.org/))
- Cabo USB compatível com a placa
- Driver USB-Serial (caso necessário):
  - [CP210x](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
  - [CH340](https://sparks.gogo.co.nz/ch340.html)

---

## 2. Instalar o Firmware MicroPython no ESP32

### 2.1 Baixar o firmware

Acesse [https://micropython.org/download/ESP32_GENERIC/](https://micropython.org/download/ESP32_GENERIC/) e baixe a versão estável mais recente (`.bin`).

### 2.2 Instalar a ferramenta esptool

```bash
pip install esptool
```

### 2.3 Apagar a flash do ESP32

Conecte a placa e identifique a porta serial (ex.: `COM3` no Windows ou `/dev/ttyUSB0` no Linux/Mac).

```bash
esptool.py --port <PORTA> erase_flash
```

### 2.4 Gravar o firmware

```bash
esptool.py --chip esp32 --port <PORTA> --baud 460800 write_flash -z 0x1000 <ARQUIVO_FIRMWARE>.bin
```

Substitua `<PORTA>` pela porta serial da placa e `<ARQUIVO_FIRMWARE>` pelo caminho do `.bin` baixado.

---

## 3. IDE Recomendada — Thonny

O [Thonny](https://thonny.org/) é a IDE mais simples para começar com MicroPython.

1. Baixe e instale o Thonny.
2. Vá em **Ferramentas → Opções → Interpretador**.
3. Selecione **MicroPython (ESP32)** e a porta serial correspondente.
4. Clique em **OK**. O terminal inferior exibirá o prompt `>>>` do MicroPython.

### Enviar o código para o ESP32 via Thonny

- Abra o arquivo `main.py` no Thonny.
- Vá em **Arquivo → Salvar como...** e escolha **Dispositivo MicroPython**.
- Salve como `main.py` para que o código rode automaticamente ao ligar a placa.

---

## 4. Estrutura de Arquivos no ESP32

| Arquivo   | Descrição |
|-----------|-----------|
| `boot.py` | Executado primeiro na inicialização; configura o sistema |
| `main.py` | Código principal do experimento |

---

## Próximos Passos

- Consulte o [Mapeamento de Pinos](esp32_pinout.md) para identificar os pinos da placa.
- Acesse a pasta do experimento desejado e siga o `README.md` correspondente.
