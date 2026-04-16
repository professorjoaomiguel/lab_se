# Lab SE — Laboratório de Sistemas Embarcados

Repositório oficial de experimentos práticos para a disciplina de **Sistemas Embarcados**, sob orientação do **Prof. Me. João Miguel Lac Roehe**.

Este projeto utiliza a linguagem **MicroPython** para programar o microcontrolador **ESP32** (em formato Arduino UNO) acoplado ao **Shield Multifuncional 9-em-1**.

---

## 📖 Sobre o Projeto

O **Lab SE** foi estruturado para fornecer uma trilha de aprendizado prática, partindo de conceitos básicos de GPIO (Entrada/Saída Digital) até o uso de conversores Analógico-Digital (ADC) e Modulação por Largura de Pulso (PWM).

### 🎯 Objetivos de Aprendizado
- Compreender a arquitetura de pinagem do ESP32 e o mapeamento de shields.
- Dominar a sintaxe básica de MicroPython para controle de hardware.
- Implementar lógica de debounce, filtragem de sensores (média de amostras) e controle proporcional.

---

## 🛠️ Requisitos e Ferramentas

### Hardware
- **ESP32 UNO** (Consulte a [**Documentação Técnica do ESP32**](docs/esp32_tecnico.md)).
- **Shield 9-em-1** (Consulte a [**Documentação Técnica dos Componentes**](docs/componentes.md)).

### Software (Língua Oficial: Português)
- **IDE Recomendada:** [Thonny IDE](https://thonny.org/).
- **Firmware:** MicroPython v1.19 ou superior.
- **Ferramenta de Flash:** `esptool.py`.

> 💡 **Dica:** Consulte o arquivo [**GEMINI.md**](GEMINI.md) para atalhos do Thonny e dicas de fluxo de trabalho.

---

## 📂 Estrutura dos Experimentos

Os laboratórios estão organizados na pasta `experiments/`. Cada experimento segue este padrão:

- `README.md`: Explicação teórica, componentes e tabela de pinagem.
- `template.py`: **Arquivo do Aluno.** Contém a estrutura base e marcações `# TODO` para implementação.
- `main.py`: Solução de referência do professor.

### 🧪 Lista de Experimentos Disponíveis

| # | Experimento | Conceitos Chave | Periféricos |
|---|---|---|---|
| 01 | [Pisca-pisca](experiments/01_pisca_pisca/) | Saída Digital, Temporização (Hello World) | LED D12, D13 |
| 02 | [Botões](experiments/02_botoes/) | Entrada Digital, Pull-up, Debounce | SW1, SW2 |
| 03 | [LDR + LEDs](experiments/03_ldr_leds/) | ADC, **Lógica de Histerese** | LDR, LED Azul/Vermelho |
| 04 | [RGB + PWM](experiments/04_rgb_ldr/) | PWM, **Modularização (utils.map_value)** | LED RGB, LDR |
| 05 | [Sensor LM35](experiments/05_lm35/) | ADC, **Filtragem (Média de Amostras)** | LM35 |
| 06 | [Potenciômetro](experiments/06_potenciometro/) | ADC, **Controle de Brilho (Dimer)** | Potenciômetro, LED D12 |
| 07 | [Buzzer](experiments/07_buzzer/) | PWM, **Geração de Tons Musicais** | Buzzer, Botões |
| 08 | [Sensor DHT11](experiments/08_dht11/) | Digital, **Protocolo One-Wire** | DHT11, LEDs |
| 09 | [Wi-Fi IoT](experiments/09_wifi/) | Redes, **Web Server e Sockets** | Wi-Fi, Sensores |

---

## 🚀 Como Iniciar as Atividades

Siga os passos abaixo para preparar seu ambiente e começar os experimentos:

1. **Clone este repositório:**
   Abra o terminal e digite:
   ```bash
   git clone https://github.com/professorjoaomiguel/lab_se.git
   cd lab_se
   ```

2. **Crie sua branch pessoal:**
   Para organizar seu trabalho, crie uma branch com seu nome completo (sem espaços):
   ```bash
   git checkout -b seu-nome-sobrenome
   ```

3. **Configure o ESP32:** Siga o [Guia de Setup](docs/setup.md) para gravar o firmware MicroPython.

4. **Suba a biblioteca utilitária:** No Thonny, salve o arquivo `lib/utils.py` na raiz do seu dispositivo ESP32.

5. **Desenvolva os Experimentos:**
   - Escolha o experimento da semana (ex: `experiments/01_pisca_pisca/`).
   - Abra o `template.py` e preencha seu nome e data.
   - Complete os desafios indicados nos comentários `# TODO`.
   - Teste no hardware pressionando **F5** no Thonny.
   - Responda à **Reflexão Obrigatória** no final do arquivo.

6. **Salve seu progresso (Commit):**
   ```bash
   git add .
   git commit -m "Concluído experimento X"
   ```

---

## 🤖 Uso de Inteligência Artificial
Incentivamos o uso da IA como tutor. Antes de começar, leia o [**Guia de Uso Saudável de IA**](docs/guia_ia.md). Lembre-se: o código deve ser seu, a IA apenas te ajuda a entender o caminho.

## ✅ Checklist de Entrega por Experimento
Para que sua atividade seja validada, você deve cumprir:
1. **Etapa Intermediária:** Hardware validado (print ou componente operando).
2. **Etapa Final:** Implementação completa da lógica proposta.
3. **Reflexão Técnica:** Preenchimento da pergunta teórica no `template.py`.
4. **Explicação Oral:** Capacidade de explicar qualquer linha do código se solicitado.

---

## 📚 Referência Bibliográfica Principal

Este laboratório é fundamentado no livro:
> **IoT com MicroPython e NodeMCU** — *Oliveira & Zanetti, Novatec 2022*.  
> Consulte o arquivo [referencias.md](docs/referencias.md) para o mapeamento completo de capítulos.

---

## 🎓 Professor Responsável
**Prof. Me. João Miguel Lac Roehe**  
Faculdade de Tecnologia SENAI Porto Alegre  
📧 [joao.roehe@senairs.org.br](mailto:joao.roehe@senairs.org.br)

---

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.
