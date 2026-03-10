# MCP – Agente de Criação de Formulários Fluig Conecta (projeto isolado)

Este repositório é **autocontido**: contém o servidor MCP, a documentação e as rules necessárias para o agente de criação de formulários Fluig.

## Estrutura

```
mcp-fluig-formularios/
├── server.py              # Servidor MCP (lê docs/ e rules/ desta pasta)
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── README.md
├── docs/                  # Documentação embutida
│   ├── style-guide-Conecta.md
│   ├── prompt-criar-formulario.md
│   ├── instrucoes-agente.md
│   ├── manual-desenvolvedor-formularios-fluig.md
│   └── manual-configuracao-mcp-equipe-dev.md
├── rules/                 # Rules (ex-.cursor/rules)
│   ├── fluig-forms.mdc
│   ├── fluig-events.mdc
│   ├── fluig-anexos.mdc
│   ├── fluig-pai-filho.mdc
│   ├── fluig-datasets.mdc
│   ├── fluig-voyager-2.0.mdc
│   └── fluig-javascript.mdc
├── .vscode/
│   └── mcp.json           # Configuração MCP para VS Code
└── .cursor/
    └── mcp.json.example   # Exemplo para Cursor
```

## Uso rápido

1. Clone ou copie esta pasta para onde quiser (projeto separado do FLUIG-CONECTA).
2. Crie o ambiente e instale dependências:
   ```powershell
   cd mcp-fluig-formularios
   py -3 -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Configure o Cursor ou o VS Code conforme **docs/manual-configuracao-mcp-equipe-dev.md**.
   - No manual, onde estiver “caminho do projeto” ou “FLUIG-CONECTA”, use o **caminho desta pasta** (mcp-fluig-formularios).
   - **Command** no MCP: `...\mcp-fluig-formularios\.venv\Scripts\python.exe`
   - **Args:** `server.py` (e **cwd** ou working directory: `...\mcp-fluig-formularios`) ou caminho completo de `server.py` em **args**.

## Recursos expostos (URIs)

| URI | Descrição |
|-----|-----------|
| `fluig-conecta://docs/style-guide` | Style Guide |
| `fluig-conecta://docs/prompt-criar-formulario` | Prompt criar formulário |
| `fluig-conecta://docs/instrucoes-agente` | Instruções do agente |
| `fluig-conecta://docs/manual-desenvolvedor-formularios` | Manual desenvolvedor |
| `fluig-conecta://rules/fluig-forms` | Rule formulários |
| `fluig-conecta://rules/fluig-events` | Rule eventos |
| `fluig-conecta://rules/fluig-anexos` | Rule anexos |
| `fluig-conecta://rules/fluig-pai-filho` | Rule pai-filho |
| `fluig-conecta://rules/fluig-datasets` | Rule datasets |
| `fluig-conecta://rules/fluig-voyager-2` | Rule Voyager 2.0 |
| `fluig-conecta://rules/fluig-javascript` | Rule JavaScript |
| `fluig-conecta://contexto/criar-formulario` | Contexto agregado |

No **macOS/Linux**, edite `.vscode/mcp.json` e use `.venv/bin/python` no `command`.

## Requisitos

- Python 3.10+
- Cursor ou VS Code 1.99+ (com MCP)

## Documentação completa

- **Configuração passo a passo (equipe DEV):** [docs/manual-configuracao-mcp-equipe-dev.md](docs/manual-configuracao-mcp-equipe-dev.md)

Projeto Fluig Conecta – MCP Agente de Formulários (versão isolada).
