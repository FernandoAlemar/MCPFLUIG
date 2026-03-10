# Prompt para criar formulário a partir de documentação

Use este texto ao enviar uma nova documentação/spec para criação de formulário. Assim as regras do projeto serão aplicadas automaticamente.

---

**Como usar:** copie o bloco abaixo e cole na sua mensagem junto com a documentação (ou anexe este arquivo com `@docs/prompt-criar-formulario.md`).

---

## Instrução para o assistente

Crie o formulário Fluig a partir da documentação que envio, aplicando **todos** os padrões do projeto:

1. **Rules e style guide:** siga @.cursor/rules/fluig-forms.mdc e @docs/style-guide-Conecta.md (seções 6 e 7).

2. **Estrutura:** pasta `forms/Nome_do_Formulario/` com arquivos:
   - `Nome_do_Formulario.html` (template base, painéis, campos conforme doc)
   - `custom.js` (eventos, zooms, controle de painéis por atividade; **não** declarar constantes de atividades)
   - `custom_valida.js` (validações)
   - `events/displayFields.js` (constantes, preenchimento automático, injeção no cliente)

3. **Constantes de atividades (formulário com workflow):**
   - **Apenas** em `displayFields.js`: declarar `var INICIO = 0;` e as constantes com os **sequence** do processo (ecm30).
   - Condição padrão para início/solicitação: `if (activity == SOLICITACAO || activity == INICIO)`.
   - Injetar no cliente `currentTask`, `MODE`, `INICIO` e todas as constantes via `customHTML.append("<script>...")`.
   - No `custom.js` **não** declarar constantes de atividades; usar só as variáveis injetadas.

4. **custom_valida.js (padrão widget_code_repository):**
   - Incluir no HTML o script `/widget_code_repository/resources/js/widget_code_repository.js`.
   - Usar `var beforeSendValidate = function (numState, nextState) { ... }`, `arrError = [];`, `campoObrig = [];`, `var obrigatorios = $('.obrigatorio:visible');`, `verificaCampos(obrigatorios);`.
   - Nos **labels** dos campos obrigatórios adicionar `class="obrigatorio"`.
   - Validações extras por atividade: usar **sequence** do processo (numState) e `arrError.push('mensagem')`; ao final, se `arrError.length > 0`, formatar e dar `throw error` (mensagem "Por favor, verifique os alertas abaixo." + lista numerada).

5. **Convenções:** IDs em camelCase; painéis com prefixo `panel_`; zooms com prefixo `zoom`; campos hidden de ID com prefixo `id`.

6. **Escolha única (Sim/Não ou opções):** usar **switch** conforme @docs/style-guide-Conecta.md (seção 3.8), **mesmo que a documentação diga "radio button"**. Um switch por opção, com `class="switch switch-success"`, `switch-input` no input e `switch-button` no label do toggle.

7. Se a documentação mencionar processo/workflow, informe o nome do processo ou o arquivo `.process`/ecm30 para alinhar os números das atividades (sequence).

---

**Exemplo de mensagem:**

> Aplicar as regras de @docs/prompt-criar-formulario.md. Segue a documentação do formulário [colar ou anexar a spec].
