# Manual de Configuração – MCP Agente de Formulários (Equipe DEV)

Este manual permite que qualquer desenvolvedor configure sozinho o **MCP (Model Context Protocol)** do agente de criação de formulários Fluig Conecta, desde os pré-requisitos até a confirmação de que está funcionando.

**Se você está neste repositório isolado (mcp-fluig-formularios):** a “pasta do projeto” é a raiz do clone (onde estão `server.py`, `docs/`, `rules/`). Onde o manual citar “FLUIG-CONECTA” ou “mcp-formularios-fluig”, use o **caminho desta pasta** ao configurar o MCP (command, cwd, args).

---

## Índice

1. [O que você precisa ter e conferir](#1-o-que-você-precisa-ter-e-conferir)
2. [Passo 1: Clonar/abrir o repositório](#2-passo-1-clonarabrir-o-repositório)
3. [Passo 2: Instalar Python e criar o ambiente](#3-passo-2-instalar-python-e-criar-o-ambiente)
4. [Passo 3: Instalar dependências do MCP](#4-passo-3-instalar-dependências-do-mcp)
5. [Passo 4: Configurar o MCP no Cursor](#5-passo-4-configurar-o-mcp-no-cursor) (e [no VS Code](#configurar-no-vs-code))
6. [Passo 5: Reiniciar o Cursor](#6-passo-5-reiniciar-o-cursor)
7. [Passo 6: Verificar se está funcionando](#7-passo-6-verificar-se-está-funcionando)
8. [Problemas comuns](#8-problemas-comuns) (incl. [“Python was not found” / Microsoft Store](#python-was-not-found--microsoft-store-windows), [Erro "caminho especificado" / ENOENT](#erro-o-sistema-não-pode-encontrar-o-caminho-especificado--enoent))

---

## 1. O que você precisa ter e conferir

Antes de começar, confira:

| Item | Como verificar |
|------|-----------------|
| **Cursor** instalado | Abra o Cursor. Versão recente (recomendado 0.40+). |
| **Python 3.10 ou superior** | No terminal: `python --version` ou `py -3 --version`. Deve mostrar 3.10, 3.11, 3.12 etc. |
| **Acesso ao repositório** | Você consegue clonar ou já tem a pasta do projeto (mcp-fluig-formularios) no seu computador. |
| **Pasta do projeto** | Deve conter `server.py`, `requirements.txt`, `README.md` e as pastas `docs/` e `rules/`. |

Se **Python não estiver instalado** ou o comando `python` abrir a Microsoft Store:

- **Windows:** baixe em [python.org/downloads](https://www.python.org/downloads/) e na instalação marque **“Add Python to PATH”**. Depois **feche e abra de novo** o terminal.
- Se mesmo assim o terminal disser **“Python was not found”** ou abrir a Microsoft Store, veja a seção [“Python was not found” / Microsoft Store (Windows)](#python-was-not-found--microsoft-store-windows) em Problemas comuns.
- **macOS/Linux:** use o gerenciador do sistema (ex.: `brew install python@3.11`) ou o site oficial.

---

## 2. Passo 1: Clonar/abrir o repositório

1. Clone o repositório (se ainda não tiver) ou abra a pasta do projeto no Cursor (ex.: **mcp-fluig-formularios** ou FLUIG-CONECTA).
2. Confira se na raiz existem:
   ```
   server.py
   requirements.txt
   pyproject.toml
   README.md
   docs/
   rules/
   ```
3. Anote o **caminho completo** da pasta do projeto no seu PC (ex.: `D:\projetos\mcp-fluig-formularios`). Você usará esse caminho na configuração do MCP.

---

## 3. Passo 2: Instalar Python e criar o ambiente

O MCP roda com um ambiente virtual (**venv**) dentro de `mcp-formularios-fluig` para não misturar com outros projetos.

### Windows (PowerShell ou CMD)

```powershell
cd CAMINHO_DO_PROJETO
python -m venv .venv
.venv\Scripts\activate
```
(No repositório isolado, CAMINHO_DO_PROJETO é a pasta mcp-fluig-formularios; no FLUIG-CONECTA, use `CAMINHO_DO_PROJETO\mcp-formularios-fluig`.)

Se der **“Python was not found”** ou abrir a Microsoft Store, use o **launcher** do Windows em vez de `python`:

```powershell
py -3 -m venv .venv
.venv\Scripts\activate
```

Ou instale o Python por [python.org](https://www.python.org/downloads/) com **“Add Python to PATH”** e desative os atalhos da Microsoft Store (veja [Problemas comuns](#python-was-not-found--microsoft-store-windows)).

Você deve ver `(.venv)` no início da linha do terminal.

### macOS / Linux

```bash
cd CAMINHO_DO_PROJETO/mcp-formularios-fluig
python3 -m venv .venv
source .venv/bin/activate
```

Substitua `CAMINHO_DO_PROJETO` pelo caminho real (ex.: `D:\FLUIG\FLUIG-CONECTA` no Windows).

---

## 4. Passo 3: Instalar dependências do MCP

Ainda com o venv ativado (deve aparecer `(.venv)` no terminal):

```bash
pip install -r requirements.txt
```

Aguarde a instalação. Ao final, deve aparecer algo como “Successfully installed mcp-...”.

**Conferir:** rode:

```bash
python -c "from mcp.server.fastmcp import FastMCP; print('OK')"
```

Se aparecer `OK`, as dependências estão corretas.

**Conferir que o `python.exe` do venv existe (evita erro ao iniciar o MCP):**

- **Windows (PowerShell ou CMD):**
  ```powershell
  dir "CAMINHO_DO_PROJETO\mcp-formularios-fluig\.venv\Scripts\python.exe"
  ```
- **macOS/Linux:**
  ```bash
  ls CAMINHO_DO_PROJETO/mcp-formularios-fluig/.venv/bin/python
  ```

Se aparecer “arquivo não encontrado” ou “No such file”, volte ao **Passo 2** e **Passo 3** e crie o venv / instale as dependências de novo. Só depois preencha o `mcp.json` com esse caminho.

---

## 5. Passo 4: Configurar o MCP no Cursor

Você pode usar **a interface do Cursor** ou o **arquivo de configuração**. Escolha uma opção.

### Opção A: Pela interface do Cursor

1. Abra **Cursor**.
2. Vá em **File > Preferences > Settings** (ou `Ctrl+,` / `Cmd+,`).
3. Procure por **“MCP”** ou **“Tools & MCP”**.
4. Clique em **“Add new MCP server”** (ou equivalente).
5. Preencha:
   - **Name:** `fluig-formularios`
   - **Type:** **Command**
   - **Command:** caminho do executável Python do venv:
     - **Windows:** `CAMINHO_DO_PROJETO\mcp-formularios-fluig\.venv\Scripts\python.exe`
     - **macOS/Linux:** `CAMINHO_DO_PROJETO/mcp-formularios-fluig/.venv/bin/python`
   - **Args:** `server.py`
   - **Working directory (se houver):** `CAMINHO_DO_PROJETO\mcp-formularios-fluig` (Windows) ou `CAMINHO_DO_PROJETO/mcp-formularios-fluig` (macOS/Linux)

Exemplo no Windows (troque `D:\FLUIG\FLUIG-CONECTA` pelo seu caminho):

- Command: `D:\FLUIG\FLUIG-CONECTA\mcp-formularios-fluig\.venv\Scripts\python.exe`
- Args: `server.py`
- Working directory: `D:\FLUIG\FLUIG-CONECTA\mcp-formularios-fluig`

### Opção B: Pelo arquivo de configuração

O Cursor pode usar um arquivo JSON para definir os servidores MCP.

**Configuração por projeto (recomendado):**

1. Na **raiz do repositório** FLUIG-CONECTA (não dentro de `mcp-formularios-fluig`), crie ou edite o arquivo:
   - **Windows:** `.cursor\mcp.json`
   - **macOS/Linux:** `.cursor/mcp.json`
2. Coloque o conteúdo abaixo, **ajustando os caminhos** para o seu computador (use `\\` no Windows ou `/` em todos):

```json
{
  "mcpServers": {
    "fluig-formularios": {
      "command": "D:\\FLUIG\\FLUIG-CONECTA\\mcp-formularios-fluig\\.venv\\Scripts\\python.exe",
      "args": ["server.py"],
      "cwd": "D:\\FLUIG\\FLUIG-CONECTA\\mcp-formularios-fluig"
    }
  }
}
```

**Exemplo no Windows** (troque `D:\FLUIG\FLUIG-CONECTA` pelo seu caminho real):

- Em `command` e `cwd`, use barras duplas: `D:\\FLUIG\\FLUIG-CONECTA\\mcp-formularios-fluig\\.venv\\Scripts\\python.exe`
- Ou use barras normais: `"D:/FLUIG/FLUIG-CONECTA/mcp-formularios-fluig/.venv/Scripts/python.exe"`

**Configuração global (todos os projetos):**

- **Windows:** `C:\Users\SEU_USUARIO\.cursor\mcp.json`
- **macOS:** `~/.cursor/mcp.json`
- **Linux:** `~/.config/cursor/mcp.json` (ou o caminho indicado na documentação do Cursor)

Use o mesmo formato JSON acima, com os caminhos do **seu** ambiente. O campo **`cwd`** é importante: sem ele, o Cursor pode rodar o processo na pasta do usuário e o Python não encontra o `server.py`, gerando o erro “can't open file 'server.py': No such file or directory”. Se já existir outros servidores (ex.: Figma), adicione apenas o bloco `"fluig-formularios": { ... }` dentro de `"mcpServers"` — **não** crie um segundo `"mcpServers"` dentro do primeiro (estrutura correta: um único `mcpServers` contendo todos os servidores).

**Como obter o caminho exato do `python.exe` (Windows):**

1. No Explorador de Arquivos, vá até `mcp-formularios-fluig\.venv\Scripts\`.
2. Clique com o botão direito em `python.exe` → **Copiar como caminho**.
3. Use esse valor no campo `command` do `mcp.json`. No JSON, troque cada `\` por `\\` ou use barras `/`.

### Configurar no VS Code

Se você usa **Visual Studio Code** (em vez do Cursor), o MCP usa outro formato.

1. **Requisito:** VS Code 1.99+ com suporte a MCP (Copilot Chat ou recurso nativo).
2. No projeto já existe **`.vscode/mcp.json`** no formato do VS Code (`servers`, `type: "stdio"`, `command`, `args`).
3. O arquivo usa **`${workspaceFolder}`** para funcionar em qualquer pasta do projeto.
4. **Windows:** o `command` aponta para `.../mcp-formularios-fluig/.venv/Scripts/python.exe`.
5. **macOS/Linux:** edite o `command` para `${workspaceFolder}/mcp-formularios-fluig/.venv/bin/python`.
6. Comandos úteis (Paleta: `Ctrl+Shift+P` / `Cmd+Shift+P`):
   - **MCP: Open Workspace Folder MCP Configuration** — abre `.vscode/mcp.json`
   - **MCP: List Servers** — listar, iniciar ou reiniciar servidores
7. Crie o venv e instale as dependências (Passos 2 e 3) antes de usar o MCP no VS Code.

Exemplo **`.vscode/mcp.json`** (já no repositório):

```json
{
  "servers": {
    "fluig-formularios": {
      "type": "stdio",
      "command": "${workspaceFolder}/mcp-formularios-fluig/.venv/Scripts/python.exe",
      "args": ["${workspaceFolder}/mcp-formularios-fluig/server.py"]
    }
  }
}
```

No macOS/Linux use `.venv/bin/python` no `command`.

**Se no VS Code aparecer "command... was not found" ou "spawn ... ENOENT":**

1. Confirme que o `.venv` existe: na raiz do projeto, pasta `mcp-formularios-fluig`, deve existir `.venv\Scripts\python.exe` (Windows) ou `.venv/bin/python` (macOS/Linux). Se não existir, crie com `python -m venv .venv` (ou `py -3 -m venv .venv`) e `pip install -r requirements.txt` dentro dessa pasta.
2. Se o projeto estiver em um caminho **com espaço** (ex.: `D:\FLUIG CONECTA`) ou `${workspaceFolder}` não resolver, use **caminho absoluto** no `.vscode/mcp.json` em vez de `${workspaceFolder}`. Exemplo para Windows (troque pelo seu caminho real, use `\\` no JSON):
   ```json
   "command": "D:\\FLUIG\\FLUIG-CONECTA\\mcp-formularios-fluig\\.venv\\Scripts\\python.exe",
   "args": ["D:\\FLUIG\\FLUIG-CONECTA\\mcp-formularios-fluig\\server.py"]
   ```
3. Abra o VS Code **abrindo a pasta do repositório** (ex.: `D:\FLUIG\FLUIG-CONECTA`) como workspace, para que `${workspaceFolder}` aponte para o diretório certo.

---

## 6. Passo 5: Reiniciar o Cursor

1. Feche completamente o Cursor (incluindo todos os projetos).
2. Abra de novo e abra a pasta **FLUIG-CONECTA** (ou o projeto onde configurou o MCP).

O Cursor só carrega a configuração do MCP ao iniciar.

---

## 7. Passo 6: Verificar se está funcionando

Siga um dos testes abaixo para ter certeza de que o MCP está ativo e respondendo.

### Teste 1: Conferir o servidor na configuração

1. Abra **Settings** > **Tools & MCP** (ou a seção de MCP).
2. Verifique se o servidor **fluig-formularios** aparece na lista e está **habilitado** (ou sem indicação de erro).
3. Em algumas versões do Cursor, há uma lista de “Resources” ou “Tools” do MCP; se aparecer algo relacionado a `fluig-conecta://`, o servidor foi carregado.

### Teste 2: Chamada de exemplo no chat (recomendado)

1. Com o projeto **FLUIG-CONECTA** aberto no Cursor, abra o **Chat** (painel do assistente).
2. Digite exatamente a seguinte mensagem (ou algo bem parecido):

   ```
   Use o resource fluig-conecta://docs/prompt-criar-formulario e me resuma em 3 tópicos o que o assistente deve fazer ao criar um formulário.
   ```

3. Envie a mensagem.
4. **Se o MCP estiver funcionando**, o assistente conseguirá ler o conteúdo do resource e responder com um resumo baseado no arquivo `docs/prompt-criar-formulario.md` (por exemplo: seguir rules e style guide, estrutura de pastas, constantes em displayFields, custom_valida, etc.).
5. **Se não estiver funcionando**, o assistente pode dizer que não tem acesso ao resource ou que o MCP não está disponível.

### Teste 3: Outra chamada de exemplo (contexto agregado)

No chat, você também pode pedir:

```
Com base no resource fluig-conecta://contexto/criar-formulario, qual é a estrutura de pastas que um formulário Fluig deve ter neste projeto?
```

A resposta esperada deve mencionar a pasta `forms/Nome_do_Formulario/` com `events/displayFields.js`, `custom.js`, `custom_valida.js` e o HTML.

### Critério de sucesso

- O assistente responde com conteúdo que **só poderia vir** dos arquivos do projeto (prompt, style guide, rules).
- Não aparece mensagem de “resource não encontrado” ou “MCP não disponível”.

Se isso ocorrer, o MCP está configurado e funcionando.

**Se o servidor aparecer com ícone vermelho / “Error - Show Output”:** clique em **Show Output** e veja a mensagem. Se for “O sistema não pode encontrar o caminho especificado” ou **ENOENT**, siga o procedimento abaixo em [Erro "caminho especificado" / ENOENT](#erro-o-sistema-não-pode-encontrar-o-caminho-especificado--enoent).

---

## 8. Problemas comuns

| Problema | O que verificar / fazer |
|----------|---------------------------|
| **“Python não encontrado”** | Instale Python 3.10+ e marque “Add to PATH”. Reinicie o terminal e o Cursor. No `mcp.json`, use o caminho **completo** do `python.exe` do `.venv`. |
| **“No module named 'mcp'”** | O Cursor está rodando outro Python (não o do venv). Em `command` no `mcp.json`, use exatamente: `...\mcp-formularios-fluig\.venv\Scripts\python.exe` (Windows) ou `.../mcp-formularios-fluig/.venv/bin/python` (macOS/Linux). |
| **Servidor não aparece no Cursor** | Confirme que salvou o `mcp.json` e **reiniciou o Cursor** por completo. Verifique se o JSON está válido (vírgulas, aspas). |
| **“Arquivo não encontrado” ao usar um resource** | O MCP acha a raiz do projeto como “pai” da pasta `mcp-formularios-fluig`. O repositório deve estar completo (com `docs/` e `.cursor/rules/`). Se o projeto estiver em outro lugar, defina a variável de ambiente `FLUIG_PROJECT_ROOT` com o caminho da raiz do repo. |
| **Caminho com espaço ou caracteres especiais** | No JSON use barras normais `/` ou escape correto. Ex.: `"D:/Meus Projetos/FLUIG-CONECTA/mcp-formularios-fluig/.venv/Scripts/python.exe"`. |
| **"can't open file '...\\server.py': No such file or directory"** | O processo está rodando em outro diretório (ex.: pasta do usuário). **Solução 1:** Inclua **`cwd`** no `mcp.json`: `"cwd": "D:\\FLUIG\\FLUIG-CONECTA\\mcp-formularios-fluig"`. Reinicie o Cursor. **Solução 2 (se o cwd não for aplicado):** use o caminho completo do script em `args`: `"args": ["D:\\FLUIG\\FLUIG-CONECTA\\mcp-formularios-fluig\\server.py"]` (pode remover o `cwd` nesse caso). |

### "Python was not found" / Microsoft Store (Windows)

Se ao rodar `python -m venv .venv` aparecer **“Python was not found; run without arguments to install from the Microsoft Store”** ou abrir a loja da Microsoft, o Windows está usando os **atalhos de “App execution aliases”** em vez do Python instalado.

**Opção 1 – Usar o launcher do Windows (rápido)**  
Muitas instalações do Python registram o comando `py`. No PowerShell ou CMD:

```powershell
py -3 --version
```

Se aparecer a versão (ex.: 3.11.x), use para criar o venv:

```powershell
cd CAMINHO_DO_PROJETO\mcp-formularios-fluig
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Opção 2 – Instalar Python e colocar no PATH**  
1. Baixe o instalador em [python.org/downloads](https://www.python.org/downloads/) (Windows).  
2. Execute o instalador e marque **“Add python.exe to PATH”**.  
3. Conclua a instalação e **feche e abra de novo** o terminal (PowerShell/CMD).  
4. Rode `python --version`. Se aparecer a versão, use `python -m venv .venv` normalmente.

**Opção 3 – Desativar os atalhos da Microsoft Store**  
1. Abra **Configurações** do Windows → **Aplicativos** → **Recursos opcionais** (ou pesquise por “App execution aliases”).  
2. Procure por **“Aliases de execução de aplicativo”** / **“App execution aliases”**.  
3. Desative **“python.exe”** e **“python3.exe”** (que apontam para a Microsoft Store).  
4. Assim, o comando `python` passará a usar o Python instalado (se estiver no PATH).

Depois de conseguir criar o `.venv` e instalar com `pip install -r requirements.txt`, siga o Passo 4 (configurar o MCP no Cursor).

### Erro "O sistema não pode encontrar o caminho especificado" / ENOENT

Esse erro aparece no **Output** do MCP (Show Output) quando o Cursor tenta iniciar o servidor e **não encontra** o `python.exe` no caminho informado no `mcp.json`. Em geral o ambiente virtual (`.venv`) não foi criado nessa pasta ou o caminho está errado.

**Passos para corrigir:**

1. **Conferir se o arquivo existe**
   - **Windows:** no PowerShell ou CMD:
     ```powershell
     dir "D:\FLUIG\FLUIG-CONECTA\mcp-formularios-fluig\.venv\Scripts\python.exe"
     ```
     (troque `D:\FLUIG\FLUIG-CONECTA` pelo **caminho real** do seu projeto.)
   - Se der **“arquivo não encontrado”**, o `.venv` não existe nesse caminho.

2. **Criar o ambiente virtual e instalar dependências**
   ```powershell
   cd D:\FLUIG\FLUIG-CONECTA\mcp-formularios-fluig
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   Troque o caminho pelo do seu projeto. Depois repita o `dir` do passo 1 para confirmar que `python.exe` existe.

3. **Usar o caminho correto no `mcp.json`**
   - O valor de `command` deve ser **exatamente** o caminho completo do `python.exe` dentro de `mcp-formularios-fluig\.venv\Scripts\` (Windows) ou `.venv/bin/python` (macOS/Linux).
   - Para copiar o caminho no Windows: Explorador de Arquivos → `mcp-formularios-fluig\.venv\Scripts\` → botão direito em `python.exe` → **Copiar como caminho**. No JSON, use `\\` no lugar de `\` ou use `/`.

4. **Reiniciar o Cursor** após alterar o `mcp.json`.

---

## Resumo rápido (checklist)

- [ ] Python 3.10+ instalado e no PATH
- [ ] Repositório FLUIG-CONECTA clonado/aberto, com pasta `mcp-formularios-fluig`
- [ ] Venv criado: `python -m venv .venv` dentro de `mcp-formularios-fluig`
- [ ] Venv ativado e dependências instaladas: `pip install -r requirements.txt`
- [ ] MCP configurado no Cursor (interface ou `.cursor/mcp.json`) com **caminhos absolutos** do seu PC
- [ ] Cursor reiniciado
- [ ] Teste no chat com: “Use o resource fluig-conecta://docs/prompt-criar-formulario e me resuma…”
- [ ] Resposta do assistente condizente com o conteúdo do projeto → MCP funcionando

---

**Dúvidas:** consulte o `README.md` dentro de `mcp-formularios-fluig` ou o time que mantém o projeto.

**Projeto:** Fluig Conecta – MCP Agente de Criação de Formulários.
