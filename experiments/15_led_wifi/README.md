# Experimento 15 — Controle de LED via Web (Wi-Fi)

## Objetivo

Controlar os LEDs D12 e D13 remotamente através de uma página HTML servida pelo próprio ESP32, acessada via navegador em qualquer dispositivo conectado à mesma rede Wi-Fi.

## Componentes Utilizados

| Componente         | Pino GPIO |
|--------------------|-----------|
| LED azul (D12)     | GPIO 12   |
| LED vermelho (D13) | GPIO 13   |

## Como Funciona

O ESP32 conecta-se à rede Wi-Fi informada e abre um servidor TCP na porta 80. A cada requisição HTTP recebida:

1. A primeira linha da requisição é lida para identificar o caminho (`/d12/on`, `/d12/off`, `/d13/on`, `/d13/off`).
2. O LED correspondente é ligado ou desligado.
3. A página HTML de controle é enviada de volta ao navegador.

| Caminho HTTP | Ação        |
|--------------|-------------|
| `/d12/on`    | Liga D12    |
| `/d12/off`   | Desliga D12 |
| `/d13/on`    | Liga D13    |
| `/d13/off`   | Desliga D13 |

## Configuração

Edite as constantes no início do `main.py`:

```python
SSID  = "SEU_SSID"
SENHA = "SUA_SENHA"
```

## Circuito

Os LEDs já estão integrados no Shield. O ESP32 precisa estar conectado à mesma rede Wi-Fi do dispositivo que acessará a página.

## Código

Carregue o arquivo `main.py` no ESP32 e anote o IP exibido no Shell. Abra `http://<IP>` no navegador.

## Exemplo de Saída Serial

```
Conectando ao Wi-Fi...
Conectado! Acesse http://192.168.1.42
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 5** — Comunicação em rede › **Wi-Fi integrado**, **Soquetes** e **Controle pela internet**  
> Disponível na biblioteca para consulta presencial.
