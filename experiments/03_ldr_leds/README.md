# Experimento 03 — Fotocélula (LDR) e Histerese

## Objetivos
1. **Intermediário:** Realizar a leitura analógica (ADC) do LDR e entender a variação de valores conforme a luz ambiente.
2. **Final:** Criar uma "Luz de Emergência" que liga o LED Vermelho no escuro e o apaga na claridade, utilizando **Histerese** para evitar que o LED pisque em níveis intermediários de luz.

## Componentes
- LDR (GPIO 1)
- LED Vermelho (GPIO 13)

## Entregáveis
- Relatório dos valores lidos no claro e no escuro.
- Código com os dois limiares de histerese definidos.

---

## 🤖 Dica de Prompt para IA
> "Estou no Experimento 03. Preciso implementar uma lógica de Histerese para um sensor LDR no MicroPython. **Não me dê o código.** Explique o que é histerese e como usar dois valores de comparação (limiar alto e baixo) em vez de apenas um para evitar que o LED fique piscando instavelmente quando a luz está no limite do sensor."
