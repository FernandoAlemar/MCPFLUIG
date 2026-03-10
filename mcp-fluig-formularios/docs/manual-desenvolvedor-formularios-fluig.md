# Manual do Desenvolvedor – Formulários Fluig

Este manual explica **como** e **por que** seguir os padrões de formulários HTML do projeto Conecta. Use-o como referência no dia a dia e consulte o **Style Guide** (`docs/style-guide-Conecta.md`) para detalhes de implementação.

---

## Sumário

1. [Visão geral](#1-visão-geral)
2. [Estrutura do formulário](#2-estrutura-do-formulário)
3. [Onde cada coisa roda: servidor x cliente](#3-onde-cada-coisa-roda-servidor-x-cliente)
4. [Constantes de atividades e workflow](#4-constantes-de-atividades-e-workflow)
5. [displayFields.js – passo a passo](#5-displayfieldsjs--passo-a-passo)
6. [custom.js – o que fazer e o que evitar](#6-customjs--o-que-fazer-e-o-que-evitar)
7. [Convenções de nomenclatura](#7-convenções-de-nomenclatura)
8. [Checklist ao criar ou alterar um formulário](#8-checklist-ao-criar-ou-alterar-um-formulário)
9. [Referências](#9-referências)

---

## 1. Visão geral

Formulários Fluig HTML são usados em processos (workflow). Eles têm:

- **HTML**: estrutura e campos (cliente).
- **custom.js**: interações, zooms, exibição de painéis (cliente).
- **custom_valida.js**: validações antes de enviar (cliente).
- **events/displayFields.js**: preenchimento automático, regras por atividade, injeção de variáveis (servidor).

O servidor executa o `displayFields.js` ao carregar o formulário; em seguida, a página é enviada ao navegador com os dados e scripts injetados. O cliente executa `custom.js` e `custom_valida.js` no navegador.

---

## 2. Estrutura do formulário

Cada formulário fica em uma pasta com o **nome do formulário** (ex.: `Analise_divergencias_financeiras`):

```
forms/
└── Nome_do_Formulario/
    ├── events/
    │   └── displayFields.js    ← roda no servidor
    ├── custom.js              ← roda no cliente
    ├── custom_valida.js       ← roda no cliente
    └── Nome_do_Formulario.html
```

- O **nome da pasta** e do **.html** deve ser o mesmo usado no processo (formCodeId), em geral no padrão `Nome_do_Formulario`.
- O `displayFields.js` roda no **servidor** (Rhino/Java). O restante roda no **navegador**.

---

## 3. Onde cada coisa roda: servidor x cliente

| Onde | Arquivo | O que faz |
|------|---------|-----------|
| **Servidor** | `events/displayFields.js` | Lê `WKNumState`, preenche campos com `form.setValue()`, injeta variáveis/constantes no HTML. Não tem acesso ao DOM nem a jQuery da página. |
| **Cliente** | `custom.js` | Eventos de campos, zooms, mostrar/ocultar painéis com base em `currentTask` e constantes **injetadas** pelo displayFields. |
| **Cliente** | `custom_valida.js` | Validações no envio (obrigatórios via widget_code_repository, regras por atividade). |

Por isso: **constantes de atividades** são definidas no servidor (`displayFields.js`) e **enviadas** para o cliente via script injetado. No `custom.js` não declaramos essas constantes de novo.

---

## 4. Constantes de atividades e workflow

### 4.1 Por que existe essa regra

O Fluig informa a **atividade atual** do processo pela variável **WKNumState**, que é o **sequence** do estado no arquivo ecm30 do processo (não é 0, 1, 2, 3…). Cada processo pode ter sequences diferentes (ex.: Início = 4, Análise = 5, Aprovação = 14).

Se você declarar constantes **no cliente** (custom.js) com valores fixos (0, 5, 10, 15…), eles podem não bater com o WKNumState real. O resultado é painel errado na atividade errada. Por isso:

- As constantes ficam **só** no `displayFields.js` (servidor), com valores iguais ao **ecm30** do processo.
- O servidor **injeta** essas constantes na página; o `custom.js` só **usa** as variáveis já existentes (currentTask, SOLICITACAO, ANALISE_CONSULTOR, etc.).

### 4.2 Regras obrigatórias

1. **Sempre declarar** no início do `displayFields.js`:
   ```javascript
   var INICIO = 0;
   ```
   `INICIO` é padrão em todos os formulários com workflow.

2. **Demais constantes** com o **sequence** do processo (consulte o ecm30 ou o Studio):
   ```javascript
   var SOLICITACAO = 4;       // valor do “Início” no ecm30
   var ANALISE_CONSULTOR = 5;
   var APROVACAO_GESTOR = 14;
   // ... sempre conferir no ecm30
   ```

3. **Condição padrão** para “abertura/solicitação” (preencher dados do solicitante, data, etc.):
   ```javascript
   if (activity == SOLICITACAO || activity == INICIO) {
       // preencher data, solicitante, etc.
   }
   ```
   Assim cobrimos tanto o sequence real do processo (SOLICITACAO) quanto o valor genérico 0 (INICIO).

4. **Injetar** no cliente todas as variáveis que o `custom.js` precisa:
   - `currentTask` (número da atividade)
   - `MODE` (ADD, MOD, VIEW)
   - `INICIO`
   - Todas as constantes de atividades (SOLICITACAO, ANALISE_CONSULTOR, etc.)

5. **No custom.js**: não declarar constantes de atividades (nem fallback). Usar apenas as variáveis injetadas.

### 4.3 Onde pegar os números (sequence)

Abra o arquivo do processo em `workflow/.resources/NomeDoProcesso.ecm30.xml` e procure por `<sequence>` dentro de cada `<ProcessState>`. O valor de `<sequence>` é o que o Fluig envia em **WKNumState** para aquela atividade.

---

## 5. displayFields.js – passo a passo

Ordem sugerida dentro da função `displayFields(form, customHTML)`:

### 5.1 Variáveis de contexto

```javascript
var activity = getValue('WKNumState') || SOLICITACAO;
var MODE = form.getFormMode();
```

- `activity`: atividade atual (sequence).
- `MODE`: ADD (novo), MOD (edição em andamento), VIEW (somente leitura).

### 5.2 Configurações do formulário

```javascript
form.setShowDisabledFields(true);
form.setHidePrintLink(true);
```

Ajuste conforme necessidade do projeto.

### 5.3 Injetar variáveis e constantes no cliente

Monte um único bloco `<script>` e adicione ao `customHTML`:

```javascript
var customJS = "<script>";
customJS += "var currentTask = " + activity + ";";
customJS += "var MODE = '" + MODE + "';";
customJS += "var INICIO = " + INICIO + ";";
customJS += "var SOLICITACAO = " + SOLICITACAO + ";";
customJS += "var ANALISE_CONSULTOR = " + ANALISE_CONSULTOR + ";";
// ... todas as outras constantes
customJS += "</script>";
customHTML.append(customJS);
```

Assim o `custom.js` pode usar `currentTask`, `SOLICITACAO`, `ANALISE_CONSULTOR`, etc., sem declarar nada.

### 5.4 Preenchimento automático por atividade

Use a condição padrão para abertura:

```javascript
if (activity == SOLICITACAO || activity == INICIO) {
    // data da solicitação, dados do solicitante (form.setValue(...))
}
```

Para outras atividades, use as constantes correspondentes:

```javascript
if (activity == APROVACAO_GESTOR && MODE == "MOD") {
    // copiar valores, habilitar campos, etc.
}
```

Sempre que precisar do número da atividade, use a **constante** (SOLICITACAO, APROVACAO_GESTOR, etc.), não números “na mão”.

---

## 6. custom.js – o que fazer e o que evitar

### 6.1 Fazer

- Usar **apenas** as variáveis injetadas: `currentTask`, `MODE`, `SOLICITACAO`, `ANALISE_CONSULTOR`, `INICIO`, etc.
- Controlar visibilidade de painéis com `currentTask` e essas constantes (ex.: `if (currentTask == APROVACAO_GESTOR) { ... }`).
- Registrar eventos de zooms e preencher campos derivados (ex.: ao escolher colaborador, preencher departamento).
- Colocar comentário no topo lembrando que constantes vêm do displayFields e não devem ser redeclaradas.

### 6.2 Evitar

- **Não** declarar constantes de atividades no custom.js (nem `var SOLICITACAO = 4;` nem fallback com `if (typeof SOLICITACAO === 'undefined')`).
- **Não** usar números fixos para atividades (ex.: `if (currentTask == 14)`). Use a constante (`APROVACAO_GESTOR`).

---

### 6.3 custom_valida.js (padrão widget_code_repository)

- **HTML:** incluir o script `/widget_code_repository/resources/js/widget_code_repository.js` e colocar `class="obrigatorio"` nos **labels** dos campos obrigatórios.
- **Estrutura:** `var beforeSendValidate = function (numState, nextState) { ... }`, com `arrError = [];`, `campoObrig = [];`, `var obrigatorios = $('.obrigatorio:visible');`, `verificaCampos(obrigatorios);`.
- **numState:** recebe o **sequence** do processo; use esse número nas validações por atividade (ex.: `if (numState == 14) { ... }`).
- **Validações extras:** (radio, percentual, checkbox etc.) fazer `arrError.push('mensagem');` após o `verificaCampos`. Se `arrError.length > 0`, formatar mensagem "Por favor, verifique os alertas abaixo." + lista numerada e dar `throw error`.

Se as constantes não existirem no cliente (ex.: preview sem passar pelo servidor), o problema deve ser resolvido garantindo que o formulário seja sempre aberto pelo processo; não criamos fallback de constantes no custom.js.

---

## 7. Convenções de nomenclatura

- **IDs de campos:** camelCase (`nomeCompleto`, `dataSolicitacao`, `valorDivergencia`).
- **Painéis:** prefixo `panel_` + nome em camelCase (`panel_dadosColaborador`, `panel_aprovacaoGestor`).
- **Zooms:** prefixo `zoom` ou nome descritivo em camelCase (`zoomGestor`, `colaboradorResponsavel`).
- **Campos hidden que guardam ID:** prefixo `id` (`idGestor`, `idColaboradorResponsavel`, `idDiretor`).

Isso mantém o código previsível e alinhado ao Style Guide.

---

## 8. Checklist ao criar ou alterar um formulário

- [ ] Estrutura de pasta e arquivos (HTML, custom.js, custom_valida.js, events/displayFields.js).
- [ ] HTML com script widget_code_repository e labels obrigatórios com `class="obrigatorio"`.
- [ ] Campos de escolha única (Sim/Não ou opções): usar **switch** (classe `switch switch-success`, `switch-input`, `switch-button`), mesmo que a documentação mencione "radio button".
- [ ] custom_valida.js no padrão (beforeSendValidate, .obrigatorio:visible, verificaCampos, arrError/campoObrig, throw formatado); numState = sequence do processo.
- [ ] No **displayFields.js**: `var INICIO = 0;` e constantes com valores do ecm30 do processo.
- [ ] Condição de início: `if (activity == SOLICITACAO || activity == INICIO)`.
- [ ] Injeção de `currentTask`, `MODE`, `INICIO` e **todas** as constantes de atividades no cliente.
- [ ] No **custom.js**: nenhuma declaração de constantes de atividades; uso apenas das variáveis injetadas.
- [ ] IDs e painéis seguindo as convenções (camelCase, `panel_`, `id` para hidden de ID).
- [ ] Processo (formCodeId) apontando para o formulário correto (formType e formCodeId no .process, se aplicável).

---

## 9. Referências

Para configurar o **MCP** (agente de formulários) no **Cursor** ou no **VS Code**, incluindo criação de venv, definição de `mcp.json` e solução de erros comuns (Python não encontrado, ENOENT, caminho do `server.py`), consulte o **Manual de Configuração MCP**: `docs/manual-configuracao-mcp-equipe-dev.md`.

| Documento | Uso |
|-----------|-----|
| `docs/style-guide-Conecta.md` | Template HTML, campos, zooms, máscaras, seções 6 e 7 (displayFields e boas práticas). |
| `docs/manual-configuracao-mcp-equipe-dev.md` | Configuração do MCP no Cursor e no VS Code, venv, troubleshooting. |
| `.cursor/rules/fluig-forms.mdc` | Regras resumidas para o editor/IA ao trabalhar em formulários. |
| `docs/prompt-criar-formulario.md` | Prompt para criar formulário a partir de documentação aplicando estes padrões. |
| `workflow/.resources/*.ecm30.xml` | Consultar `<sequence>` de cada `<ProcessState>` para definir as constantes. |

---

*Manual alinhado ao Style Guide Conecta e às rules do projeto. Em caso de dúvida, priorize o Style Guide e as definições do ecm30 do processo.*
