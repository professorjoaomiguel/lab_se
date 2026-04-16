# Experimento 09 — Wi-Fi e Servidor Web (IoT)

## Objetivos
1. **Intermediário:** Configurar a interface de rede do ESP32 (Station Mode) e realizar o handshake com um roteador local.
2. **Final:** Desenvolver um servidor HTTP básico (Sockets) que disponibiliza dados dos sensores do shield em uma página web em tempo real.

## Componentes
- Wi-Fi interno do ESP32
- Qualquer componente do shield (ex: Potenciômetro ou LM35)

## Entregáveis
- Endereço IP exibido no terminal.
- Página HTML visualizada no navegador (PC ou Celular) com dados atualizados.

---

## 🤖 Dica de Prompt para IA
> "Estou no Experimento 09 (o desafio final). Quero conectar meu ESP32 ao Wi-Fi e rodar um servidor web simples no MicroPython. **Não me dê o código pronto.** Explique o fluxo básico: como ativar a interface `network.WLAN`, como criar um 'socket' para escutar na porta 80 e como enviar uma string HTML básica quando alguém se conecta ao IP do meu ESP32."
