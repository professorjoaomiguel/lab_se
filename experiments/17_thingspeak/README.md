# Experimento 17 — Dashboard no ThingSpeak

## Objetivo

Enviar dados de temperatura (LM35) e luminosidade (LDR) para a plataforma ThingSpeak via HTTP e visualizar gráficos em tempo real no dashboard online.

## Componentes Utilizados

| Componente       | Pino GPIO    |
|------------------|--------------|
| LM35 / LDR       | GPIO 1 (ADC) |

> **Nota:** LM35 e LDR compartilham o GPIO 1. As leituras são feitas alternadamente no mesmo objeto ADC.

## Como Funciona

1. O ESP32 conecta-se à rede Wi-Fi.
2. A cada 15 segundos (intervalo mínimo do ThingSpeak), uma requisição HTTP GET é enviada para `https://api.thingspeak.com/update` com:
   - `field1` = temperatura em °C (LM35)
   - `field2` = valor bruto do LDR (0–4095)
3. O ThingSpeak registra o dado e atualiza os gráficos do canal automaticamente.

## Configuração

1. Crie uma conta em [thingspeak.com](https://thingspeak.com).
2. Crie um **novo canal** com dois campos: `field1` (Temperatura) e `field2` (Luminosidade).
3. Copie a **Write API Key** do canal.
4. Edite as constantes no início do `main.py`:

```python
SSID          = "SEU_SSID"
SENHA         = "SUA_SENHA"
WRITE_API_KEY = "SUA_WRITE_API_KEY"
```

## Circuito

Os sensores já estão integrados no Shield. Nenhuma ligação externa é necessária.

## Código

Carregue o arquivo `main.py` no ESP32 e abra o monitor serial. Acesse o canal no ThingSpeak e observe os gráficos sendo atualizados.

## Exemplo de Saída Serial

```
Conectando ao Wi-Fi...
Wi-Fi OK: 192.168.1.42
Enviando dados ao ThingSpeak a cada 15 s...
Enviado | Temp: 27.45 °C | LDR: 2100 | Entry: 1
Enviado | Temp: 27.52 °C | LDR: 2050 | Entry: 2
```

## 📖 Referência Bibliográfica

> **IoT com MicroPython e NodeMCU** — Oliveira & Zanetti, Novatec 2022  
> **Capítulo 10** — ThingSpeak  
> Disponível na biblioteca para consulta presencial.
