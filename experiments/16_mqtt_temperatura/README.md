# Experimento 16 — Monitoramento de Temperatura via MQTT

## Objetivo

Publicar a temperatura lida pelo sensor LM35 em um broker MQTT público a cada 5 segundos, permitindo monitoramento remoto via qualquer cliente MQTT (MQTT Explorer, Node-RED, smartphone etc.).

## Componentes Utilizados

| Componente | Pino GPIO    |
|------------|--------------|
| LM35       | GPIO 1 (ADC) |

## Como Funciona

1. O ESP32 conecta-se à rede Wi-Fi.
2. Uma conexão TCP é aberta com o broker `broker.hivemq.com` na porta 1883.
3. O pacote MQTT `CONNECT` é enviado manualmente (sem biblioteca externa).
4. A cada 5 segundos, a temperatura é convertida e publicada no tópico `labse/temperatura` com um pacote `PUBLISH`.

A implementação MQTT é feita diretamente com sockets, sem dependências externas, reforçando o entendimento do protocolo.

## Configuração

Edite as constantes no início do `main.py`:

```python
SSID  = "SEU_SSID"
SENHA = "SUA_SENHA"
```

Para visualizar os dados, assine o tópico `labse/temperatura` em qualquer cliente MQTT. Sugestões:
- **MQTT Explorer** (desktop): [mqtt-explorer.com](https://mqtt-explorer.com)
- **Node-RED** com nó `mqtt in`

## Circuito

O sensor LM35 já está integrado no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial para acompanhar as publicações.

## Exemplo de Saída Serial

```
Conectando ao Wi-Fi...
Wi-Fi OK: 192.168.1.42
MQTT conectado. Publicando em: labse/temperatura
Publicado: 27.45 °C
Publicado: 27.52 °C
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 7** — Redes de sensores › **MQTT**  
> **Capítulo 8** — Node-RED  
> Disponível na biblioteca para consulta presencial.
