# Usando o Thonny IDE com o ESP32

O **Thonny** é a IDE recomendada para programar o ESP32 com MicroPython neste laboratório. Este guia mostra o fluxo de trabalho completo — do zero até rodar seu primeiro experimento.

---

## 1. Instalar o Thonny

1. Acesse [https://thonny.org](https://thonny.org) e baixe o instalador para o seu sistema operacional.
2. Execute o instalador e siga as instruções padrão.

---

## 2. Conectar o ESP32 e configurar o interpretador

1. Conecte a placa ao computador via cabo USB.
2. Abra o Thonny.
3. Vá em **Ferramentas → Opções → Interpretador**.
4. Em *"Qual tipo de interpretador você quer usar?"*, selecione **MicroPython (ESP32)**.
5. Em *"Porta"*, selecione a porta serial da placa (ex.: `COM3` no Windows, `/dev/ttyUSB0` no Linux/Mac).
6. Clique em **OK**.

> **Como identificar a porta?**  
> Windows: abra o Gerenciador de Dispositivos → Portas (COM e LPT).  
> Linux/Mac: execute `ls /dev/tty*` antes e depois de conectar a placa.

O painel inferior (*Shell*) deve exibir o prompt `>>>` — isso confirma que o Thonny está comunicando com o ESP32.

---

## 3. Testar a conexão (REPL interativo)

No painel *Shell* do Thonny, digite diretamente:

```python
print("Olá, ESP32!")
```

Pressione **Enter**. O ESP32 deve responder imediatamente. Se funcionar, o ambiente está pronto.

---

## 4. Fluxo de trabalho para cada experimento

### Passo 1 — Abrir o arquivo de template

Cada experimento possui um arquivo `template.py` com o esqueleto do código. No Thonny:

- **Arquivo → Abrir → Este computador**
- Navegue até `experiments/0X_nome_do_experimento/template.py`

### Passo 2 — Completar o código

Leia o `README.md` do experimento e preencha as partes marcadas com `# TODO` no `template.py`. O arquivo `main.py` contém a solução completa como referência.

### Passo 3 — Salvar no ESP32

Quando estiver satisfeito com o código:

1. Vá em **Arquivo → Salvar como...**
2. Na janela que aparece, escolha **Dispositivo MicroPython**.
3. Nomeie o arquivo como **`main.py`**.
4. Clique em **OK**.

> ⚠️ Salvar como `main.py` faz com que o ESP32 execute esse código automaticamente toda vez que for ligado.

### Passo 4 — Executar e monitorar

- Clique no botão ▶️ **Executar** (ou pressione **F5**) para rodar o código imediatamente.
- Acompanhe as mensagens no painel *Shell* na parte inferior da tela.
- Para interromper o programa, clique no botão ⏹️ **Parar** (ou pressione **Ctrl+C** no Shell).

### Passo 5 — Reiniciar a placa

Para reiniciar o ESP32 e executar o `main.py` salvo:

- Pressione **Ctrl+D** no painel *Shell* (soft reset), ou
- Clique no botão de reset físico da placa.

---

## 5. Gerenciar arquivos no ESP32

Para visualizar os arquivos armazenados na placa:

- Vá em **Exibir → Arquivos**
- O painel de arquivos abrirá mostrando tanto os arquivos do **seu computador** (esquerda) quanto os do **ESP32** (direita).
- Arraste arquivos entre os painéis ou clique com o botão direito para enviar, baixar ou excluir.

---

## 6. Dicas e Atalhos

| Ação | Atalho |
|------|--------|
| Executar o programa | **F5** |
| Parar o programa | **F2** / **Ctrl+C** no Shell |
| Salvar arquivo | **Ctrl+S** |
| Abrir arquivo | **Ctrl+O** |
| Aumentar fonte | **Ctrl++** |
| Soft reset (reiniciar MicroPython) | **Ctrl+D** (no Shell) |
| Hard reset (reiniciar ESP32) | **Ctrl+F2** |

---

## 7. Solução de Problemas

| Problema | Solução |
|----------|---------|
| Shell mostra `Could not connect to...` | Verifique a porta serial e se o cabo USB transmite dados (não é cabo de carga) |
| Porta não aparece na lista | Instale o driver CH340 ou CP210x; reconecte o cabo |
| `>>>` não aparece | Pressione **Ctrl+C** no Shell para interromper qualquer programa em execução |
| Código não executa ao ligar | Verifique se o arquivo foi salvo como `main.py` **no dispositivo** |
| Erro `ImportError` | O módulo pode não estar instalado; verifique o firmware do MicroPython |
