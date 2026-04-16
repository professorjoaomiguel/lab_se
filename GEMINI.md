# GEMINI.md — Diretrizes e Contexto do Lab SE

Este documento estabelece as regras de ouro, padrões técnicos e diretrizes pedagógicas para o desenvolvimento do repositório **Lab SE**. Qualquer interação deve seguir rigorosamente estes combinados.

---

## 🇧🇷 Língua Oficial
- Toda a documentação, READMEs, comentários de código e mensagens de commit devem ser em **Português (Brasil)**.
- Exceções: Comandos de sistema, palavras-chave da linguagem Python e termos técnicos universais.

## 🎓 Metodologia Pedagógica: "IA como Mentor"
O objetivo é que o aluno desenvolva autonomia. Para isso:
1. **Estrutura em Etapas:** Todo experimento deve ter uma **Etapa Intermediária** (validação técnica) e uma **Etapa Final** (projeto aplicado).
2. **Reflexão Obrigatória:** Arquivos `template.py` devem conter uma seção de reflexão técnica para evitar o "copia e cola" sem entendimento.
3. **Prompts de IA:** Cada README deve sugerir um prompt que peça à IA para atuar como tutor (explicar conceitos e dar pistas) em vez de resolver o exercício.
4. **Validação Oral:** O professor reserva-se o direito de pedir explicações sobre qualquer linha de código.

## 🛠️ Padrões Técnicos (ESP32 + MicroPython)
- **Hardware Base:** ESP32 (UNO Form Factor) + Shield Multifuncional 9-em-1.
- **Mapeamento de Pinos (Fonte da Verdade):**
  - Botões: SW1 (18), SW2 (17) — Pull-up interno.
  - LEDs: Azul (12), Vermelho (13).
  - LED RGB: Red (9), Green (10), Blue (11).
  - Sensores Analógicos: Potenciômetro (36), LDR (1), LM35 (2).
  - Sensores Digitais: DHT11 (4), Buzzer (5).
- **ADC:** Usar sempre `ADC.ATTN_11DB` e `ADC.WIDTH_12BIT`.
- **Modularização:** Funções genéricas devem estar em `lib/utils.py`.

## 💻 Fluxo de Trabalho (Git & IDE)
- **IDE:** Thonny IDE é a ferramenta padrão.
- **Atalhos Thonny:** F5 (Executar), Ctrl+C (Interromper), Ctrl+D (Soft Reset).
- **Git para Alunos:**
  1. `git clone` do repositório.
  2. Criar branch pessoal: `git checkout -b seu-nome-sobrenome`.
  3. Resolver no `template.py`.
  4. Commits descritivos.

## 🔐 Privacidade e Ideias
- Notas pedagógicas, bugs intencionais e planos de aula "de bastidores" devem ser mantidos no arquivo local **`IDEIAS.md`** (localizado fora do repositório Git) para garantir a privacidade do professor.

---
*Documento atualizado em 16 de Abril de 2026.*
