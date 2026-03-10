# Instruções e papel do agente – Fluig Conecta

Este documento descreve **como instruir o agente** e **o que o agente deve fazer** no projeto, para manter padrões e consistência.

---

## 1. Instruções gerais para o agente

### 1.1 Linguagem e tom

- Responder sempre em **Português (Brasil)**.
- Ser objetivo: priorizar respostas práticas e alterações diretas no código quando for o caso.

### 1.2 Documentos de referência obrigatória

Ao trabalhar em **formulários**, o agente deve seguir:

| Contexto | Documento |
|----------|-----------|
| Padrões de formulários | `@.cursor/rules/fluig-forms.mdc` |
| Detalhes, campos, exemplos | `@docs/style-guide-Conecta.md` (seções 6 e 7) |
| Explicação para o desenvolvedor | `@docs/manual-desenvolvedor-formularios-fluig.md` |
| Criar formulário a partir de doc | `@docs/prompt-criar-formulario.md` |

Ao trabalhar em **datasets**, seguir:

- `@.cursor/rules/fluig-datasets.mdc` (questionário, matriz de decisão, templates, nomenclatura, pasta Producao)
- **Criar dataset a partir de solicitação:** `@docs/prompt-criar-dataset.md`
- Script de normalização: `scripts/normalize-datasets.ps1`, `scripts/README-datasets.md`

Outras rules em `.cursor/rules/` (fluig-events, fluig-anexos, fluig-pai-filho, etc.) devem ser aplicadas quando o contexto for relevante.

### 1.3 Quando o usuário envia documentação para criar formulário

- Aplicar **todas** as regras de `@docs/prompt-criar-formulario.md`.
- Garantir: constantes de atividades **apenas** em `displayFields.js`, incluindo `var INICIO = 0;` e condição `if (activity == SOLICITACAO || activity == INICIO)`.
- Injetar no cliente `currentTask`, `MODE`, `INICIO` e todas as constantes; no `custom.js` **não** declarar constantes de atividades.

### 1.4 Convenções que o agente deve respeitar

- **Formulários:** IDs em camelCase; painéis com prefixo `panel_`; zooms com prefixo `zoom` ou nome descritivo; campos hidden de ID com prefixo `id`. **custom_valida.js:** padrão widget_code_repository (beforeSendValidate, `$('.obrigatorio:visible')`, verificaCampos, arrError/campoObrig, throw formatado); labels obrigatórios com `class="obrigatorio"`; numState = sequence do processo.
- **Datasets:** arquivos `.js` em `datasets/Producao/`; em conflito de nome ao normalizar, usar sufixo `_from_NomeDaPasta.js`.
- **Workflow:** números de atividades (constantes) alinhados ao **sequence** do ecm30 do processo, não a sequências fictícias (0, 5, 10, 15…).

---

## 2. O que o agente faz

O agente atua como **assistente de desenvolvimento** do projeto Fluig Conecta, dentro dos seguintes escopos.

### 2.1 Formulários HTML Fluig

- **Criar** formulários a partir de documentação/spec, aplicando o template base, estrutura de painéis e convenções do projeto.
- **Alterar** formulários existentes (novos campos, novos painéis, novas atividades) mantendo constantes apenas em `displayFields.js`, injeção no cliente e sem constantes no `custom.js`.
- **Corrigir** erros de padrão: mover constantes de atividades para `displayFields.js`, adicionar `INICIO = 0` e condição padrão, ajustar injeção de variáveis.
- **Revisar** estrutura (HTML, custom.js, custom_valida.js, displayFields.js) em relação ao Style Guide e ao manual do desenvolvedor. **custom_valida.js** deve seguir o padrão widget_code_repository (verificaCampos com .obrigatorio:visible, arrError, throw formatado).

### 2.2 Datasets

- **Criar** datasets a partir de solicitação (objetivo, volume, fonte, query), aplicando a rule `fluig-datasets.mdc`: questionário, matriz de decisão (JDBC/REST, síncrono/assíncrono), template do tipo escolhido, nomenclatura `ds_[ação]_[o_que]_[tipo]`, query otimizada, arquivo em `datasets/Producao/`. Usar `@docs/prompt-criar-dataset.md` quando o usuário pedir criação de dataset.
- Ajudar a manter datasets em `datasets/Producao/` e a usar o script de normalização (`normalize-datasets.ps1`).
- Em caso de conflito de nome ao trazer arquivos de outra pasta, aplicar o sufixo `_from_NomeDaPasta` conforme a rule e o README de datasets.

### 2.3 Processos (workflow)

- Ajudar a **vincular** formulário ao processo (formType, formCodeId no `.process` quando aplicável).
- Consultar arquivos `.process` e `.ecm30.xml` para obter os **sequence** das atividades e alinhar constantes no `displayFields.js`.

### 2.4 Documentação e regras

- **Atualizar** o Style Guide, o manual do desenvolvedor e as rules (`.cursor/rules/*.mdc`) quando novos padrões forem definidos ou ajustados.
- **Criar ou atualizar** documentos em `docs/` (manuais, prompts, instruções) quando o usuário pedir.

### 2.5 O que o agente não faz (escopo)

- Não executa o Fluig nem publica artefatos no servidor (a publicação é feita pelo desenvolvedor).
- Não altera configurações de ambiente (banco, URLs, credenciais) fora do que estiver explícito no repositório.
- Não define regras de negócio ou processos sem base em documentação ou pedido explícito do usuário.

---

## 3. Resumo rápido para o desenvolvedor

- **Quero criar um formulário:** envie a documentação e use `@docs/prompt-criar-formulario.md` para o agente aplicar as regras.
- **Quero criar um dataset:** envie objetivo, volume, fonte, query (se tiver) e use `@docs/prompt-criar-dataset.md` para o agente aplicar a rule de datasets.
- **Quero padronizar um formulário:** peça para aplicar as regras de `@.cursor/rules/fluig-forms.mdc` e do manual do desenvolvedor.
- **Quero documentar um padrão novo:** peça para atualizar o Style Guide, o manual e/ou as rules em `docs/` e `.cursor/rules/`.
- **Dúvida sobre o projeto:** o agente usa `AGENTS.md`, `docs/style-guide-Conecta.md` e `docs/manual-desenvolvedor-formularios-fluig.md` como base.

---

*Este arquivo complementa o `AGENTS.md` na raiz do projeto. Para convenções gerais do projeto, consulte `AGENTS.md`; para detalhes de formulários e do que o agente faz, use este documento.*
