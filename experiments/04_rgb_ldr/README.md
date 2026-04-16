# Experimento 04 — LED RGB e PWM

## Objetivos
1. **Intermediário:** Configurar um canal PWM e validar o controle de brilho (duty cycle) do LED Verde.
2. **Final:** Criar um sistema de iluminação inteligente onde o brilho do LED RGB se ajusta automaticamente à luz ambiente usando a função `map_value` da biblioteca `utils`.

## Componentes
- LED Verde RGB (GPIO 10)
- LDR (GPIO 1)
- Biblioteca `lib/utils.py`

## Entregáveis
- Código importando e utilizando corretamente o módulo `utils`.
- Demonstração do LED aumentando/diminuindo o brilho suavemente.

---

## 🤖 Dica de Prompt para IA
> "Estou no Experimento 04. Preciso controlar o brilho de um LED RGB usando o `machine.PWM` no MicroPython. **Não me dê o código.** Explique o que é o 'duty cycle' e como eu posso converter proporcionalmente uma leitura de sensor que vai de 0 a 4095 (ADC) para uma escala de PWM que vai de 0 a 1023."
