# Experimento 02 — Botões e Interação

## Objetivos
1. **Intermediário:** Detectar o acionamento do botão SW1 (GPIO 18) e exibir uma mensagem no terminal.
2. **Final:** Implementar uma lógica de "Toggle": cada vez que SW1 for pressionado, o LED Azul (D12) deve mudar de estado (se estava aceso, apaga; se estava apagado, acende).

## Componentes
- Botão SW1 (GPIO 18 - Pull-up)
- LED Azul (GPIO 12)

## Entregáveis
- Implementação de debounce simples.
- Funcionamento do LED como um interruptor de luz.

---

## 🤖 Dica de Prompt para IA
> "Estou no Experimento 02. Preciso usar um botão (Pull-up) para inverter o estado de um LED (lógica de Toggle) no MicroPython. **Não me dê o código.** Explique o conceito de uma variável de estado para 'lembrar' se o LED deve estar aceso ou apagado e por que preciso de um pequeno `sleep` para evitar que o botão seja lido várias vezes por causa da trepidação mecânica (debounce)."
