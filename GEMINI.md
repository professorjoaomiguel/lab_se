# GEMINI.md — Contexto do Projeto Lab SE

Este repositório é um laboratório prático para o ensino de **Sistemas Embarcados**, focado no uso do microcontrolador **ESP32** com a linguagem **MicroPython**. O hardware base utilizado é o **Shield 9-em-1**.

## 🚀 Visão Geral do Projeto

O objetivo do projeto é fornecer uma base estruturada de experimentos práticos. A língua oficial de toda a documentação e comentários deste repositório é o **Português (Brasil)**.

### Tecnologias Principais
- **Hardware:** ESP32 (NodeMCU) + Shield 9-em-1.
- **Linguagem:** MicroPython.
- **IDE Principal:** Thonny IDE.

---

## 💻 Ferramenta de Desenvolvimento: Thonny IDE

A [Thonny IDE](https://thonny.org/) é a ferramenta recomendada para este laboratório.

### Atalhos Essenciais no Thonny:
- **F5:** Executa o script atual no ESP32.
- **Ctrl + C:** Interrompe a execução do script (envia um KeyboardInterrupt para o REPL).
- **Ctrl + D:** Realiza um Soft Reset no ESP32.
- **Ctrl + S:** Salva o arquivo atual.

### Fluxo de Trabalho:
1. Conecte o ESP32 via USB.
2. Em **Configurações -> Interpretador**, selecione **MicroPython (ESP32)**.
3. Para que um código rode automaticamente ao ligar a placa, salve-o no dispositivo com o nome `main.py`.

---

## 📂 Estrutura do Repositório

- `/experiments`: Atividades práticas. Cada pasta possui um `README.md` (instruções), um `template.py` (exercício para o aluno) e um `main.py` (solução).
- `/lib`: Módulos reutilizáveis como `utils.py`.
- `/docs`: Guias detalhados de pinagem e instalação.

---

## 📝 Convenções de Desenvolvimento

- **Idioma:** Documentação, READMEs e comentários de código devem ser em **Português**.
- **Exercícios:** Alunos devem clonar o repositório e completar os arquivos `template.py`.
- **Bibliotecas:** Funções comuns (como `map_value` ou `debounce`) devem ser importadas de `lib/utils.py`.
