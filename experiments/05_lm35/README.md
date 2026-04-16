# Experimento 05 — Sensor de Temperatura LM35

## Objetivos
1. **Intermediário:** Ler o valor analógico e convertê-lo matematicamente para Voltagem (V), comparando com a medida de um multímetro (se disponível).
2. **Final:** Converter a voltagem para Temperatura (°C) e aplicar uma filtragem por **Média de Amostras** (20 leituras) para estabilizar o valor no terminal.

## Componentes
- Sensor LM35 (GPIO 2)
- [Datasheet do LM35](https://www.ti.com/lit/ds/symlink/lm35.pdf)

## Entregáveis
- Demonstração da temperatura no Shell com no máximo 0.5°C de oscilação.
- Cálculo da escala (V/°C) documentado no código.

---

## 🤖 Dica de Prompt para IA
> "Estou no Experimento 05. Tenho um sensor LM35 (analógico) e um ESP32. **Não me dê o código.** Explique como converter a leitura bruta do ADC (0 a 4095) para Voltagem, considerando que o ESP32 usa 3.3V, e depois como converter essa voltagem para Graus Celsius seguindo a regra de 10mV/°C do LM35. Além disso, me dê uma pista de como fazer uma média simples de leituras para que a temperatura não oscile tanto no monitor."
