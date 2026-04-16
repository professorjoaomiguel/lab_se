# Experimento 06 — Dimer com Potenciômetro

## Objetivos
1. **Intermediário:** Realizar a leitura do potenciômetro e converter o valor bruto (0-4095) para uma escala percentual (0-100%).
2. **Final:** Implementar um controle de intensidade (Dimer) para o LED Azul (D12), onde o giro do potenciômetro controla suavemente o brilho do LED via PWM.

## Componentes
- Potenciômetro (GPIO 36)
- LED Azul (GPIO 12 - PWM)

## Entregáveis
- Código integrando leitura analógica, mapeamento e saída PWM.
- Demonstração do LED variando de 0% a 100% de brilho.

---

## 🤖 Dica de Prompt para IA
> "Estou no Experimento 06. Preciso criar um 'Dimer' onde o potenciômetro controla o brilho de um LED no MicroPython. **Não me dê o código.** Como eu faço a ponte entre a leitura do ADC (potenciômetro) e a configuração do duty cycle do PWM (LED)? Quais funções do módulo `machine` eu devo pesquisar?"
