# Style Guide - Formulários Fluig

Guia de padrões para desenvolvimento de formulários na plataforma Fluig.

---

## Sumário

1. [Estrutura de Pastas](#1-estrutura-de-pastas)
2. [Estrutura do HTML](#2-estrutura-do-html)
3. [Campos de Formulário](#3-campos-de-formulário)
4. [JavaScript - custom.js](#4-javascript---customjs)
5. [JavaScript - custom_valida.js](#5-javascript---custom_validajs)
6. [Events - displayFields.js](#6-events---displayfieldsjs)
7. [Boas Práticas](#7-boas-práticas)
8. [Nomenclatura](#8-nomenclatura)
9. [Componente de Anexos](#9-componente-de-anexos)
10. [Tabela Pai-Filho](#10-tabela-pai-filho)
11. [Padrões Visuais Conecta](#11-padrões-visuais-conecta)
12. [Datasets](#12-datasets)  
– [Apêndice A – Por que não criar .process via style guide](#apêndice-a--por-que-não-criar-arquivo-process-via-style-guide)

---

## 1. Estrutura de Pastas

```
forms/
└── Nome_do_Formulario/
    ├── events/
    │   └── displayFields.js      # Eventos do servidor (backend)
    ├── custom.js                 # Lógica JavaScript do cliente
    ├── custom_valida.js          # Validações de campos
    └── Nome_do_Formulario.html   # Estrutura HTML do formulário
```

### Descrição dos Arquivos

| Arquivo | Descrição | Execução |
|---------|-----------|----------|
| `Nome_do_Formulario.html` | Estrutura visual do formulário | Cliente |
| `custom.js` | Lógica de interação, eventos de campos, manipulação de zooms | Cliente |
| `custom_valida.js` | Validação de campos obrigatórios antes do envio | Cliente |
| `events/displayFields.js` | Preenche campos automaticamente, controla visibilidade | Servidor |

---

## 2. Estrutura do HTML

### 2.1 Template Base

```html
<html>

<head>
    <meta charset="utf-8">
    <!-- CSS do Fluig Style Guide -->
    <link type="text/css" rel="stylesheet" href="https://style.fluig.com/css/fluig-style-guide-flat.min.css" />
    <link type="text/css" rel="stylesheet" href="/style-guide/css/fluig-style-guide.min.css" />
    
    <!-- Scripts obrigatórios -->
    <script type="text/javascript" src="/portal/resources/js/jquery/jquery.js"></script>
    <script type="text/javascript" src="/portal/resources/js/jquery/jquery-ui.min.js"></script>
    <script type="text/javascript" src="/portal/resources/js/mustache/mustache-min.js"></script>
    <script type="text/javascript" src="/style-guide/js/fluig-style-guide.min.js" charset="utf-8"></script>
    <script type="text/javascript" src="/webdesk/vcXMLRPC.js" charset="utf-8"></script>
    
    <!-- Scripts customizados (widget de utilitários) -->
    <script type="text/javascript" src="/widget_code_repository/resources/js/widget_code_repository.js" charset="utf-8"></script>
    
    <!-- Scripts do formulário -->
    <script type="text/javascript" src="custom.js"></script>
    <script type="text/javascript" src="custom_valida.js" charset="utf-8"></script>
</head>

<body>
    <div class="fluig-style-guide">
        <form name="form" role="form">
            
            <!-- Cabeçalho do Formulário -->
            <div class="page-header">
                <header class="main-header clearfix">
                    <div class="wrapper">
                        <div class="row">
                            <div class="col-md-3 text-left"></div>
                            <div class="col-md-6 title">
                                <h1 class="text-center">Título do Formulário</h1>
                            </div>
                            <div class="col-md-3 text-right">
                                <img id="companyLogoImg" src="https://www.bancorbras.com.br/assets/img/logo-bancorbras.png" alt="Logo">
                            </div>
                        </div>
                    </div>
                </header>
            </div>
            
            <!-- Painéis do Formulário -->
            <!-- ... -->
            
        </form>
    </div>
</body>

</html>
```

### 2.2 Estrutura de Painéis

```html
<div class="panel panel-default" id="panel_nomePainel">
    <div class="panel-heading">
        <h3 class="panel-title">
            <strong>Título do Painel</strong>
        </h3>
    </div>
    <div class="panel-body">
        <!-- Conteúdo do painel -->
    </div>
</div>
```

### 2.3 Grid System (Bootstrap 3)

Use o sistema de grid do Bootstrap para organizar os campos:

```html
<div class="form-group row">
    <div class="col-md-4">
        <!-- Campo 1 (4 colunas) -->
    </div>
    <div class="col-md-4">
        <!-- Campo 2 (4 colunas) -->
    </div>
    <div class="col-md-4">
        <!-- Campo 3 (4 colunas) -->
    </div>
</div>
```

| Classe | Largura | Uso Comum |
|--------|---------|-----------|
| `col-md-12` | 100% | Textarea, campos únicos |
| `col-md-6` | 50% | Campos médios |
| `col-md-4` | 33% | Campos pequenos (padrão) |
| `col-md-3` | 25% | Campos muito pequenos |

### 2.4 Estrutura Padrão - Dados do Colaborador

Todo formulário deve iniciar com **dois painéis** de dados do colaborador:

#### Painel 1 - Dados do Colaborador (Solicitante)

Campos preenchidos automaticamente via `displayFields.js`:

```html
<!--Painel Dados do Colaborador-->
<div class="panel panel-default" id="panel_dadosColaborador">
    <div class="panel-heading ">
        <h3 class="panel-title">
            <strong>Dados do Colaborador</strong>
        </h3>
    </div>
    <div class="panel-body">
        <div class="form-group row">
            <div class="col-md-4">
                <label for="dataSolicitacao">Data da Solicitação<font style="color: red">*</font></label>
                <input type="date" class="form-control required" name="dataSolicitacao" id="dataSolicitacao" readonly>
            </div>
            <div class="col-md-4">
                <label for="empresa">Empresa<font style="color: red">*</font></label>
                <input type="text" class="form-control required" name="empresa" id="empresa" readonly>
            </div>
            <div class="col-md-4">
                <label for="departamento">Departamento<font style="color: red">*</font></label>
                <input type="text" class="form-control required" name="departamento" id="departamento" readonly>
            </div>
        </div>
        <div class="form-group row">
            <div class="col-md-12">
                <label for="nomeCompleto">Nome Completo<font style="color: red">*</font></label>
                <input type="text" class="form-control required" name="nomeCompleto" id="nomeCompleto" readonly>
            </div>
        </div>
        <div class="form-group row">
            <div class="col-md-4">
                <label for="cargo">Cargo<font style="color: red">*</font></label>
                <input type="text" class="form-control required" name="cargo" id="cargo" readonly>
            </div>
            <div class="col-md-4">
                <label for="matricula">Matrícula<font style="color: red">*</font></label>
                <input type="text" class="form-control required" name="matricula" id="matricula" readonly>
            </div>
            <div class="col-md-4">
                <label for="telefone">Telefone</label>
                <input type="text" class="form-control" name="telefone" id="telefone" mask="(00)00000-0000">
            </div>
        </div>
        
        <input type="hidden" id="idfluigsolicitante" name="idfluigsolicitante">
        <input type="hidden" id="emailsolicitante" name="emailsolicitante">
    </div>
</div>
```

#### Painel 2 - Dados do Colaborador (Complemento)

Usado quando é necessário selecionar outro colaborador responsável:

```html
<!--Painel Dados do Colaborador (Complemento)-->
<div class="panel panel-default" id="panel_dadosComplementares">
    <div class="panel-heading ">
        <h3 class="panel-title">
            <strong>Dados do Colaborador</strong>
        </h3>
    </div>
    <div class="panel-body">
        <input type="hidden" id="hiddenColaboradorResponsavel" name="hiddenColaboradorResponsavel">
        <input type="hidden" id="matriculaGestorComercial" name="matriculaGestorComercial">

        <div class="form-group row">
            <div class="col-md-4">
                <label for="negocio">Negócio<font style="color: red">*</font></label>
                <select class="form-control required" id="negocio" name="negocio">
                    <option value=""></option>
                    <option value="corporativo">Corporativo</option>
                    <option value="operadora">Operadora</option>
                </select>
            </div>
            <div class="col-md-4">
                <label for="gestorComercial">Gestor Comercial<font style="color: red">*</font></label>
                <input type="zoom" class="form-control required" id="gestorComercial" name="gestorComercial"
                    data-zoom="{
                        'displayKey': 'NOME',
                        'datasetId': 'ds_usuarios_papel',
                        'filterValues': 'papel,gestor_comercial_turismo',
                        'fields': [
                            {'field': 'ID', 'label': 'Matrícula', 'standard': 'true'},
                            {'field': 'NOME', 'label': 'Nome'},
                            {'field': 'EMAIL', 'label': 'E-mail'}
                        ],
                        'result': ['ID', 'NOME', 'EMAIL']
                    }">
            </div>
            <div class="col-md-4">
                <label for="colaboradorResponsavel">Colaborador Responsável<font style="color: red">*</font></label>
                <input type="zoom" class="form-control required" id="colaboradorResponsavel" name="colaboradorResponsavel"
                    data-zoom="{
                        'displayKey': 'NOME',
                        'datasetId': 'ds_colaborador',
                        'filterValues': 'SITUACAO,A',
                        'fields': [
                            {'field': 'CHAPA', 'label': 'Matrícula', 'standard': 'true'},
                            {'field': 'NOME', 'label': 'Nome'},
                            {'field': 'EMAIL', 'label': 'E-mail'}
                        ],
                        'result': ['CHAPA', 'NOME', 'CODFIL', 'NOMEFIL', 'CODDEPART', 'DESCDEPART', 'CODFUNCAO', 'DESCFUNCAO', 'EMAIL']
                    }">
            </div>
        </div>
        <div class="form-group row">
            <div class="col-md-4">
                <label for="empresaColab">Empresa</label>
                <input type="text" class="form-control" id="empresaColab" name="empresaColab" readonly>
            </div>
            <div class="col-md-4">
                <label for="departamentoColab">Departamento</label>
                <input type="text" class="form-control" id="departamentoColab" name="departamentoColab" readonly>
            </div>
            <div class="col-md-4">
                <label for="cargoColab">Cargo</label>
                <input type="text" class="form-control" id="cargoColab" name="cargoColab" readonly>
            </div>
        </div>
        <div class="form-group row">
            <div class="col-md-4">
                <label for="matriculaColab">Matrícula</label>
                <input type="text" class="form-control" id="matriculaColab" name="matriculaColab" readonly>
            </div>
            <div class="col-md-4">
                <label for="emailColab">E-mail</label>
                <input type="text" class="form-control" id="emailColab" name="emailColab" readonly>
            </div>
            <div class="col-md-4">
                <label for="gestorImediato">Gestor Imediato</label>
                <input type="text" class="form-control" id="gestorImediato" name="gestorImediato" readonly>
            </div>
        </div>
    </div>
</div>
```

#### Datasets Utilizados

| Dataset | Uso | Campos Principais |
|---------|-----|-------------------|
| `ds_usuarios_papel` | Busca usuários por papel | `ID`, `NOME`, `EMAIL` |
| `ds_colaborador` | Busca colaboradores ativos | `CHAPA`, `NOME`, `EMAIL`, `NOMEFIL`, `DESCDEPART`, `DESCFUNCAO` |

#### Preenchimento Automático (displayFields.js)

```javascript
// Dados do solicitante via REST
var user = getUser(getValue("WKUser"));
var funcionario = dadosfunc(user.mail);

form.setValue('dataSolicitacao', year + '-' + month + '-' + day);
form.setValue('nomeCompleto', funcionario.NOME);
form.setValue('empresa', funcionario.NOMEFIL);
form.setValue('departamento', funcionario.DESCDEPART);
form.setValue('matricula', funcionario.MATRICULA);
form.setValue('cargo', funcionario.FUNCAO);
```

---

## 3. Campos de Formulário

### 3.1 Campo de Texto Simples

```html
<div class="col-md-4">
    <label for="nomeCampo">Label do Campo<font style="color: red">*</font></label>
    <input type="text" class="form-control required" name="nomeCampo" id="nomeCampo">
</div>
```

### 3.2 Campo Somente Leitura

```html
<input type="text" class="form-control" name="campo" id="campo" readonly>
```

### 3.3 Campo de Data

```html
<div class="col-md-4">
    <label for="dataCampo">Data<font style="color: red">*</font></label>
    <input type="date" class="form-control required" name="dataCampo" id="dataCampo">
</div>
```

### 3.4 Campo Select

```html
<div class="form-group col-md-4">
    <label for="selectCampo" class="obrigatorio">Label<font style="color: red">*</font></label>
    <select id="selectCampo" name="selectCampo" class="form-control">
        <option value=""></option>
        <option value="opcao1">Opção 1</option>
        <option value="opcao2">Opção 2</option>
    </select>
</div>
```

### 3.5 Campo Textarea

```html
<div class="col-md-12 form-group">
    <label class="control-label obrigatorio" for="textareaCampo">
        Descrição<font style="color: red">*</font>
    </label>
    <textarea class="form-control" id="textareaCampo" name="textareaCampo" 
              rows="4" placeholder="Mínimo 200 caracteres." minlength="200"></textarea>
</div>
```

### 3.6 Campo Zoom (Autocomplete com Dataset)

```html
<div class="form-group col-md-4">
    <label for="zoomCampo" class="obrigatorio">Campo Zoom<font style="color: red">*</font></label>
    <input type="zoom" class="form-control" id="zoomCampo" name="zoomCampo"
        data-zoom="{
            'displayKey':'CAMPO_EXIBICAO',
            'datasetId':'nome_dataset',
            'fields':[
                {'field':'CAMPO1','label':'Label 1','standard':true,'visible':'true'},
                {'field':'CAMPO2','label':'Label 2','visible':'false'}
            ]
        }">
</div>
```

#### Propriedades do Zoom

| Propriedade | Descrição |
|-------------|-----------|
| `displayKey` | Campo que será exibido no input após seleção |
| `datasetId` | Nome do dataset que alimenta o zoom |
| `fields` | Array de campos a serem exibidos na busca |
| `standard` | Define como campo de busca padrão |
| `visible` | Mostra/oculta coluna na listagem |
| `maximumSelectionLength` | Limite de itens selecionáveis |
| `placeholder` | Texto placeholder |

### 3.7 Campo Hidden (Controle)

```html
<input type="hidden" id="campoControle" name="campoControle" value="valor_padrao">
```

### 3.8 Campo Switch (escolha única – Sim/Não ou opções)

**Regra:** Mesmo que a documentação do formulário mencione "radio button" ou "seleção única", utilizar **switch** conforme este style guide.

Um switch por opção (mesmo `name` para agrupar):

```html
<div class="col-md-6">
    <label class="obrigatorio">Opções<font style="color: red">*</font></label>
    <div class="switch switch-success">
        <label>Sim</label>
        <input class="switch-input" type="radio" value="Sim" name="opcaoCampo" id="opcaoCampoSim" />
        <label class="switch-button" for="opcaoCampoSim">Toggle</label>
    </div>
    <div class="switch switch-success">
        <label>Não</label>
        <input class="switch-input" type="radio" value="Não" name="opcaoCampo" id="opcaoCampoNao" />
        <label class="switch-button" for="opcaoCampoNao">Toggle</label>
    </div>
</div>
```

Exemplo com valor customizado (ex.: aprovação):

```html
<div class="switch switch-success">
    <label>Aprovado</label>
    <input class="switch-input" type="radio" value="aprovado" name="emitirParecer" id="emitirParecerAprovado" />
    <label class="switch-button" for="emitirParecerAprovado">Toggle</label>
</div>
```

### 3.9 Campo Checkbox

```html
<div class="col-md-3">
    <label>Concordo<font style="color: red">*</font></label>
    <div class="checkbox">
        <label>
            <input type="checkbox" id="deAcordo" name="deAcordo" value="Sim"> Eu concordo
        </label>
    </div>
</div>
```

### 3.10 Campo com Máscara

```html
<!-- Telefone -->
<input type="text" class="form-control" name="telefone" id="telefone" mask="(00)00000-0000">

<!-- Data -->
<input type="text" class="form-control" name="data" id="data" mask="00/00/0000" placeholder="dd/mm/aaaa">

<!-- Valor monetário -->
<input type="text" class="form-control" name="valor" id="valor" mask="#.##0,00" data-reverse="true" placeholder="R$ 0,00">

<!-- Percentual -->
<div class="input-group">
    <input type="text" class="form-control" id="percentual" name="percentual" maxlength="3" placeholder="1 a 100">
    <span class="input-group-addon">%</span>
</div>
```

| Máscara | Formato | Exemplo |
|---------|---------|---------|
| `(00)00000-0000` | Telefone | (61)99999-9999 |
| `00/00/0000` | Data | 10/02/2026 |
| `#.##0,00` | Moeda | 1.234,56 |
| `000.000.000-00` | CPF | 123.456.789-00 |

---

## 4. JavaScript - custom.js

### 4.1 Estrutura Base

```javascript
$(document).ready(function(){
    
    // ========================================
    // 1. EVENTOS DE CAMPOS
    // ========================================
    
    // Evento de mudança em switch/radio (escolha única)
    $("input[name=campoSwitch]").click(function () {
        if (this.value == "Sim") {
            $('.classeCondicional').show();
        } else {
            $('.classeCondicional').hide();
            $('#campoLimpar').val("");
        }
    });
    
    // Evento de change em select
    $('#selectCampo').change(function () {
        if ($(this).val() == "opcao1") {
            $(".divCondicional").show('slow');
        } else {
            $(".divCondicional").hide('slow');
        }
    });
    
    // ========================================
    // 2. INICIALIZAÇÃO DE ESTADO
    // ========================================
    
    // Verifica estado inicial dos campos
    if ($('input[name="campoSwitch"]:checked').val() == 'sim') {
        $('.classeCondicional').show();
    }
    
    // ========================================
    // 3. CONTROLE POR ATIVIDADE
    // ========================================
    
    if (currentTask == 0 || currentTask == 4) {
        // Atividade inicial
        let divs = "#panel_painel1";
        let hidediv = "#panel_painel2,#panel_painel3";
        disablefield(divs);
        hidedivs(hidediv);
    }
    
    if (currentTask == 5) {
        // Atividade 5
        let divs = "#panel_painel1";
        let hidediv = "#panel_painel2";
        disablefield(divs);
        hidedivs(hidediv);
    }
    
});

// ========================================
// FUNÇÕES DE ZOOM
// ========================================

/**
 * Callback quando item é selecionado no zoom
 * @param {Object} selectedItem - Item selecionado
 */
function setSelectedZoomItem(selectedItem) {
    var id = selectedItem.inputId.split('___')[0];
    var index = selectedItem.inputId.split('___')[1];
    
    if (id == 'zoomCampo') {
        // Lógica após seleção
        $('#campoHidden').val(selectedItem.CAMPO);
        
        // Recarrega outro zoom com filtro
        reloadZoomFilterValues('outroZoom', 'filtro,' + selectedItem.VALOR);
    }
}

/**
 * Callback quando item é removido do zoom
 * @param {Object} removedItem - Item removido
 */
function removedZoomItem(removedItem) {
    var id = removedItem.inputId.split('___')[0];
    
    if (id == 'zoomCampo') {
        $('#campoHidden').val('');
        window['outroZoom'].clear();
    }
}

// ========================================
// FUNÇÕES UTILITÁRIAS
// ========================================

/**
 * Oculta divs especificadas
 * @param {string} idDivs - Seletores separados por vírgula
 */
function hidedivs(idDivs) {
    $(idDivs).css('display', 'none');
}

/**
 * Busca dados via Dataset
 * @param {string} email - Email do colaborador
 * @returns {Object} Dados do colaborador
 */
function getDadosColaborador(email) {
    var constraints = new Array();
    var dataset = null;
    
    constraints.push(DatasetFactory.createConstraint("mail", email, email, ConstraintType.MUST));
    dataset = DatasetFactory.getDataset("colleague", null, constraints, null);
    
    if (dataset.values.length > 0) {
        return dataset.values[0];
    }
    
    return null;
}

/**
 * Valida se usuário pertence a um papel
 * @param {string} userId - ID do usuário
 * @param {string} roleId - ID do papel
 * @returns {boolean}
 */
function validaPapel(userId, roleId) {
    var filtro = new Array();
    filtro.push(DatasetFactory.createConstraint('workflowColleagueRolePK.colleagueId', userId, userId, ConstraintType.MUST));
    filtro.push(DatasetFactory.createConstraint('workflowColleagueRolePK.roleId', roleId, roleId, ConstraintType.MUST));
    
    var dataset = DatasetFactory.getDataset('workflowColleagueRole', null, filtro, null);
    
    return dataset.values.length > 0;
}

/**
 * Formata data para padrão YYYY-MM-DD
 * @param {Date} date - Objeto Date
 * @returns {string} Data formatada
 */
function formatDate(date) {
    var dd = date.getDate();
    var mm = date.getMonth() + 1;
    var yyyy = date.getFullYear();

    if (dd < 10) dd = '0' + dd;
    if (mm < 10) mm = '0' + mm;

    return yyyy + '-' + mm + '-' + dd;
}
```

---

## 5. JavaScript - custom_valida.js

**Padrão obrigatório:** usar a biblioteca **widget_code_repository** e a estrutura abaixo. No HTML, incluir o script da biblioteca e adicionar `class="obrigatorio"` nos **labels** dos campos obrigatórios. O parâmetro `numState` recebe o **sequence** do processo (ecm30); use esse valor nas validações por atividade.

### 5.1 Estrutura Base

```javascript
///////////////////////////////////////////////////////
// VALIDAÇÃO CAMPOS FORMULÁRIO
// numState:  número da atividade atual  (int)
// nextState: número da atividade destino (int)
///////////////////////////////////////////////////////

var beforeSendValidate = function (numState, nextState) {
    
    arrError = [];    // Array global de erros
    campoObrig = [];  // Array global de campos obrigatórios
    
    // Busca todos os campos com classe 'obrigatorio' que estão visíveis
    var obrigatorios = $('.obrigatorio:visible');
    
    // Função do widget_code_repository que verifica os campos
    verificaCampos(obrigatorios);
    
    // Validações customizadas por atividade
    if (numState == 5) {
        // Validações específicas da atividade 5
        if ($('#campo').val() == '') {
            arrError.push("Campo X é obrigatório na atividade 5");
        }
    }
    
    // Exibe erros se houver
    if (arrError.length > 0) {
        var error = "Por favor, verifique os alertas abaixo.\r\t";
        
        for (var i = 0; i < arrError.length; i++) {
            var count = i + 1;
            if (parseInt(i) > 0) {
                arrError[i] = "\r\t" + count + " - " + arrError[i];
            } else {
                arrError[i] = count + " - " + arrError[i];
            }
            error += arrError[i];
        }
        
        throw error;
    }
    
}
```

### 5.2 Marcação de Campos Obrigatórios

Para que a validação funcione, adicione a classe `obrigatorio` no **label** do campo. O HTML do formulário deve incluir o script do widget_code_repository antes do custom_valida.js:

```html
<label for="campo" class="obrigatorio">Label<font style="color: red">*</font></label>
```

---

## 6. Events - displayFields.js

### 6.1 Constantes de atividades (fonte única)

Em formulários vinculados a processo (workflow):

- **Constantes de atividades ficam apenas em `events/displayFields.js`.** Não declarar em `custom.js` (nem fallback).
- **Sempre declarar:** `var INICIO = 0;` (atividade inicial genérica). Demais constantes com os **sequence** do processo (WKNumState), conforme o ecm30. Não use sequência fictícia (0, 5, 10, 15…) para as demais.
- **Padrão para atividade de início/solicitação:** usar sempre a condição `if (activity == SOLICITACAO || activity == INICIO)` ao preencher dados do solicitante ou tratar abertura do formulário.
- **Injeção no cliente:** o `displayFields.js` deve injetar `currentTask`, `MODE`, `INICIO` e **todas** as constantes de atividades via script no `customHTML`, para o `custom.js` usar no controle de painéis e regras.

Exemplo de constantes no displayFields.js (valores alinhados ao ecm30 do processo):

```javascript
// Sempre declarar (padrão)
var INICIO = 0;

// Constantes de atividades (WKNumState / sequence do processo)
var SOLICITACAO = 4;       // ex.: Início
var ANALISE_CONSULTOR = 5;
var PARECER_SUPERVISOR = 16;
var PARECER_COORDENACAO = 18;
var APROVACAO_GESTOR = 14;
var APROVACAO_DIRETOR = 28;
var TERMO_CIENCIA = 23;
var DESCONTO_FOLHA = 31;
var BAIXA_PENDENCIA = 33;
```

Exemplo de condição padrão para preenchimento na solicitação/início:

```javascript
if (activity == SOLICITACAO || activity == INICIO) {
    // Data da solicitação, dados do solicitante, etc.
}
```

Exemplo de injeção no cliente (dentro de displayFields):

```javascript
var customJS = "<script>";
customJS += "var currentTask = " + activity + ";";
customJS += "var MODE = '" + MODE + "';";
customJS += "var INICIO = " + INICIO + ";";
customJS += "var SOLICITACAO = " + SOLICITACAO + ";";
customJS += "var ANALISE_CONSULTOR = " + ANALISE_CONSULTOR + ";";
// ... demais constantes
customJS += "</script>";
customHTML.append(customJS);
```

No `custom.js`, usar apenas as variáveis injetadas (ex.: `currentTask`, `SOLICITACAO`, `ANALISE_CONSULTOR`) sem redeclará-las.

### 6.2 Estrutura Base

```javascript
/**
 * Função executada no servidor ao carregar o formulário
 * @param {Object} form - Objeto do formulário
 * @param {Object} customHTML - Objeto para adicionar HTML/Scripts customizados
 */
function displayFields(form, customHTML) {
    
    var activity = getValue('WKNumState');  // Atividade atual
    var MODE = form.getFormMode();          // Modo: ADD, MOD, VIEW
    var mail = fluigAPI.getUserService().getCurrent().getEmail();
    
    // ========================================
    // 1. INJETAR VARIÁVEIS E CONSTANTES NO CLIENTE
    // ========================================
    
    customHTML.append("<script>");
    customHTML.append("var currentTask='" + activity + "';");
    customHTML.append("function getMode(){ return '" + MODE + "'};");
    // Se houver workflow: injetar também constantes de atividades (SOLICITACAO, etc.)
    customHTML.append("</script>");
    
    // ========================================
    // 2. CONFIGURAÇÕES DO FORMULÁRIO
    // ========================================
    
    form.setShowDisabledFields(true);   // Mostra campos desabilitados
    form.setHidePrintLink(true);        // Oculta link de impressão
    
    // ========================================
    // 3. PREENCHIMENTO AUTOMÁTICO POR ATIVIDADE
    // ========================================
    
    if (activity == 0 || activity == 4) {
        // Atividade inicial - preenche dados do solicitante
        
        var today = new Date();
        var year = today.getFullYear();
        var month = (today.getMonth() + 1).toString().padStart(2, '0');
        var day = today.getDate().toString().padStart(2, '0');
        
        form.setValue('dataSolicitacao', year + '-' + month + '-' + day);
        form.setValue('idfluigsolicitante', getValue('WKUser'));
        form.setValue('emailsolicitante', mail);
        
        // Busca dados do funcionário
        var funcionario = dadosfunc(mail);
        form.setValue('nomeCompleto', funcionario.NOME);
        form.setValue('empresa', funcionario.NOMEFIL);
        form.setValue('departamento', funcionario.DESCDEPART);
    }
    
}

// ========================================
// FUNÇÕES AUXILIARES (SERVIDOR)
// ========================================

/**
 * Busca dados do funcionário via API REST
 * @param {string} email - Email do funcionário
 * @returns {Object} Dados do funcionário
 */
function dadosfunc(email) {
    var clientService = fluigAPI.getAuthorizeClientService();
    
    var data = {
        companyId: getValue('WKCompany') + '',
        serviceCode: 'SERVICO_REST',
        endpoint: '/endpoint?email=' + email,
        method: 'get',
        timeoutService: '100'
    };
    
    var vo = clientService.invoke(JSON.stringify(data));
    var objdata = JSON.parse(vo.getResult());
    
    return objdata;
}

/**
 * Busca usuário pelo colleagueId
 * @param {string} colleagueId - ID do colaborador
 * @returns {Object} Dados do usuário
 */
function getUser(colleagueId) {
    var constraints = new Array();
    var dataset = null;
    var user = { "colleagueName": "" };
    
    constraints.push(DatasetFactory.createConstraint(
        "colleaguePK.colleagueId", colleagueId, colleagueId, ConstraintType.MUST
    ));
    
    dataset = DatasetFactory.getDataset("colleague", null, constraints, null);
    
    if (dataset.rowsCount > 0) {
        user.login = dataset.getValue(0, "login");
        user.colleagueName = dataset.getValue(0, "colleagueName");
        user.mail = dataset.getValue(0, "mail");
        user.id = dataset.getValue(0, "colleaguePK.colleagueId");
    } else {
        log.error("Usuário não encontrado: " + colleagueId);
        throw("Usuário não encontrado: " + colleagueId);
    }
    
    return user;
}
```

### 6.3 Variáveis Globais do Workflow (getValue)

| Variável | Descrição |
|----------|-----------|
| `WKNumState` | Número da atividade atual |
| `WKUser` | ID do usuário logado |
| `WKCompany` | Código da empresa |
| `WKNumProces` | Número da solicitação |
| `WKNextState` | Próxima atividade |
| `WKCardId` | ID do card/formulário |

---

## 7. Boas Práticas

### 7.1 Organização do Código

- Separar lógica de exibição (`custom.js`) da validação (`custom_valida.js`)
- Em formulários com workflow: constantes de atividades apenas em `displayFields.js`; em `custom.js` não declarar essas constantes (usar as injetadas)
- Usar comentários para separar seções do código
- Documentar funções com JSDoc

### 7.2 Performance

- Evitar consultas a datasets dentro de loops
- Usar `disablefield()` em vez de `readonly` para melhor UX
- Carregar dados de zooms sob demanda com filtros

### 7.3 Manutenibilidade

- Usar IDs de painéis prefixados: `panel_nomePainel`
- Usar classes CSS para controle de visibilidade: `.showCondicao`, `.hideCondicao`
- Centralizar funções utilitárias no `widget_code_repository`

### 7.4 Segurança

- Nunca expor dados sensíveis em campos hidden
- Validar dados tanto no cliente quanto no servidor
- Usar mecanismos de atribuição corretos no workflow

---

## 8. Nomenclatura

### 8.1 Convenções de Nomes

| Elemento | Padrão | Exemplo |
|----------|--------|---------|
| ID de painel | `panel_camelCase` | `panel_dadosColaborador` |
| ID de campo | `camelCase` | `nomeCompleto` |
| Classe de controle | `camelCase` | `showDiretor`, `hideAprendiz` |
| Dataset | `ds_snake_case` | `ds_func_all_sinc` |
| Papel (Role) | `snake_case` | `cargos_salarios` |

### 8.2 Prefixos Recomendados

| Prefixo | Uso | Exemplo |
|---------|-----|---------|
| `zoom` | Campos de zoom | `zoomDiretor` |
| `btn` | Botões | `btnSalvar` |
| `chk` | Checkboxes | `chkAceite` |
| `rad` | Radio buttons | `radTipo` |
| `txt` | Textareas | `txtObservacao` |
| `sel` | Selects | `selEmpresa` |

---

## 9. Componente de Anexos

O componente customizado de anexos permite associar arquivos específicos a campos do formulário, utilizando a aba de anexos nativa do Fluig.

### 9.1 Estrutura de Arquivos

Para utilizar o componente de anexos, adicione os seguintes arquivos ao formulário:

```
forms/
└── Nome_do_Formulario/
    ├── anexos.js       # Lógica do componente de anexos
    ├── style.css       # Estilos do componente
    └── ...
```

### 9.2 Inclusão no HTML

```html
<head>
    <!-- CSS do componente de anexos -->
    <link type="text/css" rel="stylesheet" href="style.css"/>
    
    <!-- Script do componente de anexos -->
    <script type="text/javascript" src="anexos.js" charset="utf-8"></script>
</head>
```

### 9.3 Estrutura HTML do Componente

#### Campo de Anexo Simples

```html
<div class="col-md-3">
    <div class="form-group">
        <label class="control-label">Nome do Documento</label>
        <div class="componentAnexo">
            <div class="input-group">
                <!-- Campo hidden com descrição do anexo -->
                <input type="hidden" class="descAnexo" name="fdDocumento" value="Descrição do Documento" />
                <!-- Campo visível com nome do arquivo físico -->
                <input type="text" id="fnDocumento" name="fnDocumento" class="form-control inputAnexo input-sm" 
                       placeholder="Selecione um arquivo" readonly />
            </div>
            <div class="icones">
                <!-- Botão de Upload/Delete -->
                <button type="button" class="btnUpFile btn btn-success btn-sm" 
                        data-acao="upload" onclick="anexo(event)" title="Selecionar">
                    <i class="fluigicon fluigicon-file-upload icon-sm"></i>
                </button>
                <!-- Botão de Visualização -->
                <button style="display: none;" type="button" class="btnViewerFile btn btn-info btn-sm" 
                        data-acao="viewer" onclick="anexo(event)" title="Visualizar" disabled>
                    <i class="fluigicon fluigicon-eye-open icon-sm"></i>
                </button>
                <!-- Botão de Download -->
                <button style="display: none;" type="button" class="btnDownloadFile btn btn-info btn-sm" 
                        data-acao="download" onclick="anexo(event)" title="Download" disabled>
                    <i class="fluigicon fluigicon-download icon-sm"></i>
                </button>
            </div>
        </div>
    </div>
</div>
```

### 9.4 Classes CSS Obrigatórias

| Classe | Descrição | Elemento |
|--------|-----------|----------|
| `.componentAnexo` | Container principal do componente | `div` |
| `.descAnexo` | Campo hidden com descrição do anexo | `input hidden` |
| `.inputAnexo` | Campo de texto exibindo nome do arquivo | `input text` |
| `.btnUpFile` | Botão de upload/delete | `button` |
| `.btnViewerFile` | Botão de visualização | `button` |
| `.btnDownloadFile` | Botão de download | `button` |
| `.icones` | Container dos botões | `div` |

### 9.5 Atributos data-acao

| Valor | Ação | Descrição |
|-------|------|-----------|
| `upload` | Selecionar arquivo | Abre seletor de arquivos |
| `viewer` | Visualizar anexo | Abre visualizador do Fluig |
| `download` | Baixar arquivo | Faz download do anexo |
| `delete` | Remover anexo | Remove da aba de anexos |

### 9.6 CSS do Componente (style.css)

```css
.componentAnexo {
    display: flex;
    align-items: center;
    flex-wrap: nowrap;
}

.componentAnexo .input-group {
    flex-grow: 1;
    position: relative;
}

.componentAnexo .inputAnexo {
    color: blue !important;
    border-radius: 0 !important;
}

.componentAnexo .icones {
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.componentAnexo .icones .btn {
    outline: none !important;
    outline-offset: unset !important;
    border-radius: 0;
    padding-left: 7px;
    padding-right: 7px;
    margin-left: 3px;
}
```

### 9.7 Funções Principais do anexos.js

#### Função Controladora Principal

```javascript
/**
 * Direciona para cada função correspondente ao valor do atributo data-acao
 * @param {object} event - Elemento que sofreu o evento click
 */
function anexo(event) {
    const acao = event.currentTarget.getAttribute("data-acao");
    const inputFile = $(event.currentTarget).parent().parent().find(".inputAnexo")[0];
    const fileDescription = $(event.currentTarget).parent().parent().find(".descAnexo").val();
    
    if (acao == "upload") uploadFile(fileDescription, inputFile.id);
    if (acao == "viewer") viewerFile(fileDescription);
    if (acao == "download") downloadFile(fileDescription, inputFile.id);
    if (acao == "delete") removeFileConfirm(fileDescription, inputFile.id);
}
```

#### Upload de Arquivo

```javascript
/**
 * Envia arquivos para a aba Anexos do Fluig
 * @param {String} fileDescription - Descrição do arquivo na aba anexos
 * @param {String} idInput - Id do campo onde o nome físico é gravado
 */
function uploadFile(fileDescription, idInput) {
    if (!getMobile()) {
        var tabAttachments = parent.document.getElementById("tab-attachments");
        if (tabAttachments) {
            var element = parent.document.getElementById("ecm-navigation-inputFile-clone");
            if (element && document.createEvent) {
                element.setAttribute("data-on-camera", "true");
                element.setAttribute("data-file-name-camera", fileDescription);
                element.setAttribute("data-inputNameFile", idInput);
                element.click();
            }
        }
    }
}
```

#### Atualização de Estado dos Botões

```javascript
/**
 * Altera o estado e visibilidade dos botões de anexos
 * @param {String} idInput - Id do campo do arquivo
 * @param {String} acao - Ação: delete ou upload
 * @param {String} btn - Botão secundário: download ou viewer
 */
function btnState(idInput, acao, btn) {
    let btnUpFile = $(`#${idInput}`).parent().parent().find(".btnUpFile");
    let btnDownloadFile = $(`#${idInput}`).parent().parent().find(".btnDownloadFile");
    let btnViewerFile = $(`#${idInput}`).parent().parent().find(".btnViewerFile");
    
    if (acao == "delete") {
        btnUpFile.removeClass("btn-success").addClass("btn-danger");
        btnUpFile.attr({ 'data-acao': acao, 'title': 'Excluir' });
        btnUpFile.find("i").removeClass("fluigicon-file-upload").addClass("fluigicon-trash");
        if (btn == "download") btnDownloadFile.prop("disabled", false).show();
        if (btn == "viewer") btnViewerFile.prop("disabled", false).show();
    }
    
    if (acao == "upload") {
        btnUpFile.removeClass("btn-danger").addClass("btn-success");
        btnUpFile.attr({ 'data-acao': acao, 'title': 'Selecionar' });
        btnUpFile.find("i").removeClass("fluigicon-trash").addClass("fluigicon-file-upload");
        btnDownloadFile.prop("disabled", true).hide();
        btnViewerFile.prop("disabled", true).hide();
    }
}
```

### 9.8 Configuração no displayFields.js

```javascript
function displayFields(form, customHTML) {
    var MODE = form.getFormMode();
    var ATIVIDADE = Number(getValue("WKNumState"));
    
    // No modo ADD, definir as descrições dos anexos
    if (MODE == "ADD") {
        form.setValue("fdDocumento", "Descrição do Documento");
        form.setValue("fdComprovante", "Comprovante");
        // ... outros campos de descrição
    }
    
    // Injetar função getMode para uso no client-side
    var customJS = "<script>";
    customJS += "function getMode(){ return '" + MODE + "'};";
    customJS += "displayBtnFiles();"; // Atualiza estado dos botões
    customJS += "</script>";
    customHTML.append(customJS);
}
```

> **Importante:** Os campos `fdDescricao` (hidden com descrição) devem ter seus valores setados no `displayFields.js` quando em modo ADD, especialmente se estiverem bloqueados pelo `enableFields`. Caso contrário, terão valores zerados e as funções de anexo não funcionarão.

### 9.9 Controle por Atividade (custom.js)

```javascript
var INICIO = 1;
var APROVACAO = 2;

$(document).ready(function() {
    // Remove botão de upload em atividades que não devem permitir alteração
    if (getAtividade() != INICIO) {
        invisibleBtnUpload("fnDocumento");
    }
    
    if (getAtividade() != APROVACAO) {
        invisibleBtnUpload("fnComprovante");
    }
});
```

### 9.10 Validação de Anexos (custom_valida.js)

```javascript
var beforeSendValidate = function(numState, nextState) {
    let hasError = "";
    
    // Validar se o anexo existe na aba de anexos
    if (invalidFile("fnDocumento")) {
        hasError += "<li>Anexo <b>Documento</b> não encontrado.</li>";
    }
    
    // Validar anexos em tabela pai-filho
    hasError += invalidFilesTable("dependentes", "fnRegistroNascDep");
    
    if (hasError) {
        throw (`<b>Erros encontrados:</b><ul>${hasError}</ul>`);
    }
};
```

### 9.11 Funções de Validação

```javascript
/**
 * Verifica se o anexo existe na aba de anexos do Fluig
 * @param {String} fileDescription - Descrição do arquivo
 * @return {Boolean} - true se existir
 */
function hasFileFluig(fileDescription) {
    const anexos = parent.ECM.attachmentTable.getData();
    for (let i = 0; i < anexos.length; i++) {
        if (fileDescription == anexos[i].description) {
            return true;
        }
    }
    return false;
}

/**
 * Verifica se o campo do anexo está preenchido mas o arquivo não existe
 * @param {String} idInput - Id do campo
 * @return {Boolean} - true se inválido
 */
function invalidFile(idInput) {
    const inputNameFile = $(`#${idInput}`).val();
    if (inputNameFile) {
        let fileDescription = $(`#${idInput}`).parent().find(".descAnexo").val();
        return !hasFileFluig(fileDescription);
    }
    return false;
}
```

---

## 10. Tabela Pai-Filho

Tabelas pai-filho permitem adicionar múltiplos registros relacionados a um formulário principal.

### 10.1 Estrutura HTML Básica

```html
<div class="panel panel-info">
    <div class="panel-heading">
        <h3 class="panel-title"><b>Dependentes</b></h3>
    </div>
    <div class="panel-body">
        <div class="row">
            <div class="col-md-12">
                <div class="table-responsive">
                    <table tablename="dependentes" id="tblDependente" class="table table-bordered tabelaPaiFilho" 
                           nodeletebutton="true" noaddbutton="true">
                        <thead class="fs-display-none">
                            <tr>
                                <td></td>
                                <td></td>
                                <td class="tdDeleteRow"></td>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <!-- Coluna de numeração -->
                                <td class="fs-v-align-middle fs-font-bold count" style="width: 1%;"></td>
                                
                                <!-- Conteúdo da linha -->
                                <td>
                                    <div class="row">
                                        <div class="col-md-2">
                                            <div class="form-group">
                                                <label class="control-label">Código</label>
                                                <input type="text" class="form-control input-sm" 
                                                       id="dependenteCodigo" name="dependenteCodigo" readonly />
                                            </div>
                                        </div>
                                        <div class="col-md-6">
                                            <div class="form-group">
                                                <label class="control-label">Nome</label>
                                                <input type="text" class="form-control input-sm" 
                                                       id="dependenteNome" name="dependenteNome" />
                                            </div>
                                        </div>
                                        <!-- Campo de anexo na tabela -->
                                        <div class="col-md-4">
                                            <div class="form-group">
                                                <label class="control-label">Documento</label>
                                                <div class="componentAnexo">
                                                    <div class="input-group">
                                                        <input type="hidden" class="descAnexo" name="fdDocDep" />
                                                        <input type="text" id="fnDocDep" name="fnDocDep" 
                                                               class="form-control inputAnexo input-sm" 
                                                               placeholder="Selecione um arquivo" readonly />
                                                    </div>
                                                    <div class="icones">
                                                        <button type="button" class="btnUpFile btn btn-success btn-sm" 
                                                                data-acao="upload" onclick="anexo(event)" title="Selecionar">
                                                            <i class="fluigicon fluigicon-file-upload icon-sm"></i>
                                                        </button>
                                                        <button style="display: none;" type="button" 
                                                                class="btnViewerFile btn btn-info btn-sm" 
                                                                data-acao="viewer" onclick="anexo(event)" title="Visualizar" disabled>
                                                            <i class="fluigicon fluigicon-eye-open icon-sm"></i>
                                                        </button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </td>
                                
                                <!-- Coluna de ação (excluir) -->
                                <td class="fs-v-align-middle fs-text-center tdDeleteRow" style="width: 1%;">
                                    <div>
                                        <i class="fluigicon fluigicon-trash icon-md fs-xs-padding fs-cursor-pointer fs-color-danger" 
                                           title="Remover" onclick="destroyRowDependente(this)"></i>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
            <!-- Botão para adicionar nova linha -->
            <div class="col-md-12 btnAddNewRow" id="btnAddNewRowDependente">
                <button class="btn btn-sm btn-success" onClick="addNewRowDependente()">Novo Dependente</button>
            </div>
        </div>
    </div>
</div>
```

### 10.2 Atributos Importantes da Table

| Atributo | Descrição |
|----------|-----------|
| `tablename` | Nome único da tabela (usado nas APIs do Fluig) |
| `nodeletebutton="true"` | Remove botão padrão de exclusão |
| `noaddbutton="true"` | Remove botão padrão de adicionar |

### 10.3 Funções JavaScript (custom.js)

#### Adicionar Nova Linha

```javascript
/**
 * Adiciona uma nova linha na tabela pai-filho
 */
function addNewRowDependente() {
    const tablename = "dependentes";
    const idByTimestamp = (new Date().getTime()).toString(32);  // ID único
    const indice = wdkAddChild(tablename);  // API nativa do Fluig
    
    // Define valores iniciais
    $(`#dependenteCodigo___${indice}`).val(idByTimestamp).prop("readonly", true);
    
    // Define descrição do anexo (importante para componente de anexos)
    $(`#fdDocDep___${indice}`).val(`Documento ${idByTimestamp}`);
    
    // Atualiza numeração das linhas
    tableLineCount(tablename);
}
```

#### Remover Linha

```javascript
/**
 * Remove uma linha da tabela pai-filho
 * @param {Element} event - Elemento que disparou o evento
 */
function destroyRowDependente(event) {
    const tabela = $(event).closest('table')[0];
    const tablename = tabela.getAttribute("tablename");
    const indice = getIndice($(event).closest('tr').find("input")[0].id);
    const codigo = $(`#dependenteCodigo___${indice}`).val() || "Código em branco";
    
    // Dados do anexo (se houver)
    const inputFileName = $(event).closest('tr').find(".inputAnexo").val();
    const inputFileDesc = $(event).closest('tr').find(".descAnexo").val();
    
    FLUIGC.message.confirm({
        message: `Deseja remover o registro de código <b>${codigo}</b>?`,
        title: 'Confirmação',
        labelYes: 'Sim, remover',
        labelNo: 'Cancelar',
    }, function(result) {
        if (result) {
            fnWdkRemoveChild(event);  // API nativa do Fluig
            
            // Remove anexo associado (se houver)
            if (inputFileName && inputFileDesc) {
                removeFile(inputFileDesc);
            }
            
            tableLineCount(tablename);
        }
    });
}
```

#### Obter Índice da Linha

```javascript
/**
 * Retorna o índice da linha com base no id de um campo
 * @param {String} id - ID de um campo (ex: "dependenteNome___8")
 * @return {String} - Índice (ex: "8")
 */
function getIndice(id) {
    return id.split('___').pop();
}
```

#### Numeração Automática de Linhas

```javascript
/**
 * Insere numeração em cada linha da tabela
 * @param {String} tablename - Nome da tabela (false para todas)
 */
function tableLineCount(tablename) {
    let atributo = tablename ? `[tablename='${tablename}']` : "[tablename]";
    
    $.each($(atributo), function(index) {
        const tabelaRow = $(this).find('tbody tr').not(':first');
        tabelaRow.each(function(i) {
            tabelaRow.eq(i).find('td.count').html(`<span>${i + 1}</span>`);
        });
    });
}
```

### 10.4 Configuração no displayFields.js

```javascript
function displayFields(form, customHTML) {
    var MODE = form.getFormMode();
    var ATIVIDADE = Number(getValue("WKNumState"));
    var customJS = "<script>";
    
    // Em modo VIEW: remove botões de ação
    if (MODE == "VIEW") {
        customJS += "$('.btnAddNewRow').remove();";
        customJS += "$('.tdDeleteRow').remove();";
    }
    
    // Em atividades específicas: remove edição da tabela
    if (ATIVIDADE != INICIO) {
        // Remove botão de upload para cada linha existente
        var totalLinhas = form.getChildrenIndexes("dependentes");
        for (var i = 0; i < totalLinhas.length; i++) {
            var inputId = "fnDocDep___" + totalLinhas[i];
            customJS += "invisibleBtnUpload('" + inputId + "');";
        }
        customJS += "$('.btnAddNewRow').remove();";
        customJS += "$('.tdDeleteRow').remove();";
    }
    
    customJS += "tableLineCount();"; // Numera linhas ao carregar
    customJS += "</script>";
    customHTML.append(customJS);
}
```

### 10.5 Validação de Anexos em Tabela Pai-Filho

```javascript
/**
 * Valida anexos em todas as linhas de uma tabela pai-filho
 * @param {String} tablename - Nome da tabela
 * @param {String} idInput - ID base do campo de anexo
 * @return {String} - HTML com erros encontrados
 */
function invalidFilesTable(tablename, idInput) {
    let errors = "";
    const countRows = $(`[tablename='${tablename}']`).find('tbody tr').not(':first');
    
    for (let i = 0; i < countRows.length; i++) {
        let indice = getIndice(countRows.eq(i).find("input")[0].id);
        let inputNameFile = $(`#${idInput}___${indice}`);
        let fileDescription = inputNameFile.parent().find(".descAnexo").val();
        
        if (inputNameFile.val() && !hasFileFluig(fileDescription)) {
            errors += `<li>Anexo <b>${inputNameFile.val()}</b> da linha <b>${i + 1}</b> não encontrado</li>`;
        }
    }
    return errors;
}
```

### 10.6 APIs Nativas do Fluig

| Função | Descrição | Retorno |
|--------|-----------|---------|
| `wdkAddChild(tablename)` | Adiciona nova linha na tabela | Índice da nova linha |
| `fnWdkRemoveChild(element)` | Remove linha da tabela | void |
| `form.getChildrenIndexes(tablename)` | Retorna array de índices | Array de strings |

### 10.7 Convenção de Nomenclatura de Campos

Em tabelas pai-filho, os campos recebem sufixo automático com o índice da linha:

| Campo Original | Campo na Linha | Exemplo |
|---------------|----------------|---------|
| `dependenteNome` | `dependenteNome___X` | `dependenteNome___0` |
| `fdDocDep` | `fdDocDep___X` | `fdDocDep___8` |

> **Nota:** O separador padrão é `___` (três underscores).

### 10.8 Boas Práticas

1. **Sempre use IDs únicos** - Gere códigos com timestamp para identificar linhas
2. **Confirme exclusão** - Use `FLUIGC.message.confirm` antes de remover
3. **Remova anexos ao excluir** - Limpe a aba de anexos quando remover uma linha
4. **Controle por atividade** - Esconda botões de ação em atividades não editáveis
5. **Numere as linhas** - Facilita referência para o usuário
6. **Valide anexos** - Verifique se anexos existem antes de enviar

---

## 11. Padrões Visuais Conecta

Esta seção documenta os padrões visuais específicos adotados pela equipe Conecta para garantir consistência em todos os formulários.

### 11.1 Cabeçalho do Formulário

O cabeçalho deve conter título centralizado e logo à direita:

```html
<div class="page-header">
    <header class="main-header clearfix">
        <div class="wrapper">
            <div class="row">
                <div class="col-md-3 text-left"></div>
                <div class="col-md-6 title">
                    <h1 class="text-center">Título do Formulário</h1>
                </div>
                <div class="col-md-3 text-right">
                    <img id="companyLogoImg" src="https://www.bancorbras.com.br/assets/img/logo-bancorbras.png" alt="Logo">
                </div>
            </div>
        </div>
    </header>
</div>
```

### 11.2 Estilo de Painéis

**SEMPRE** usar `panel-default` (cinza) em vez de `panel-primary` (azul):

```html
<!-- CORRETO -->
<div class="panel panel-default" id="panel_nomePainel">
    <div class="panel-heading">
        <h3 class="panel-title"><strong>Título do Painel</strong></h3>
    </div>
    <div class="panel-body">
        <!-- Conteúdo -->
    </div>
</div>

<!-- INCORRETO - NÃO USAR -->
<div class="panel panel-primary" id="panel_nomePainel">
```

| Classe | Visual | Uso |
|--------|--------|-----|
| `panel-default` | Cinza | **Padrão Conecta** |
| `panel-primary` | Azul | Não usar |
| `panel-success` | Verde | Casos especiais |
| `panel-danger` | Vermelho | Alertas críticos |

### 11.3 Indicador de Campo Obrigatório

Usar tag `<font>` com estilo inline para asteriscos vermelhos:

```html
<!-- CORRETO -->
<label for="campo">Nome do Campo<font style="color: red">*</font></label>

<!-- INCORRETO - NÃO USAR -->
<label for="campo">Nome do Campo<span class="text-danger">*</span></label>
```

### 11.4 Estrutura de Linhas e Colunas

Usar `form-group row` para agrupar campos na mesma linha:

```html
<!-- CORRETO -->
<div class="form-group row">
    <div class="col-md-4">
        <label for="campo1">Campo 1<font style="color: red">*</font></label>
        <input type="text" class="form-control" id="campo1" name="campo1">
    </div>
    <div class="col-md-4">
        <label for="campo2">Campo 2</label>
        <input type="text" class="form-control" id="campo2" name="campo2">
    </div>
    <div class="col-md-4">
        <label for="campo3">Campo 3</label>
        <input type="text" class="form-control" id="campo3" name="campo3">
    </div>
</div>
```

### 11.5 Espaçamento e Alinhamento

- Usar `<br>` para separação vertical entre painéis
- Manter consistência de larguras de coluna dentro do mesmo painel
- Labels sempre acima dos campos (não inline)

### 11.6 Resumo Visual

| Elemento | Padrão Conecta |
|----------|----------------|
| Painéis | `panel-default` (cinza) |
| Título | Centralizado com logo à direita |
| Obrigatório | `<font style="color: red">*</font>` |
| Grid | `form-group row` > `col-md-X` |
| Logo | URL Bancorbras oficial |

---

## 12. Datasets

### 12.1 Tipos de Datasets

Existem 4 tipos de datasets no Fluig, classificados por **fonte de dados** e **modo de execução**:

| Tipo | Fonte | Execução | Uso |
|------|-------|----------|-----|
| **JDBC Síncrono** | Banco de dados | Tempo real | Zoom simples, validações |
| **JDBC Assíncrono** | Banco de dados | Scheduler | Relatórios médios |
| **REST Síncrono** | API REST | Tempo real | Zoom, validações complexas |
| **REST Assíncrono** | API REST | Scheduler | Relatórios pesados, cargas |

### 12.2 Matriz de Decisão

```
VOLUME/COMPLEXIDADE │ TEMPO REAL = SIM  │ TEMPO REAL = NÃO
────────────────────┼───────────────────┼──────────────────
Baixo/Simples       │ JDBC Síncrono     │ JDBC Síncrono
Baixo/Média         │ REST Síncrono     │ REST Síncrono
Médio/Simples       │ JDBC Síncrono     │ JDBC Assíncrono
Médio/Média         │ REST Síncrono     │ REST Assíncrono
Alto/Qualquer       │ REST Síncrono*    │ REST Assíncrono ✓
Muito Alto          │ NÃO RECOMENDADO   │ REST Assíncrono ✓
Complexa            │ REST Síncrono     │ REST Assíncrono ✓

* Com paginação obrigatória
✓ Recomendado
```

### 12.3 Quando Usar Cada Tipo

| Cenário | Tipo Recomendado | Motivo |
|---------|------------------|--------|
| Zoom de formulário | REST/JDBC Síncrono | Dados atualizados, volume baixo |
| Relatório gerencial | REST Assíncrono | Volume alto, dados históricos |
| Dashboard | REST Assíncrono | Performance, delay aceitável |
| Validação tempo real | REST Síncrono | Precisa dado atual |
| Carga de dados | REST Assíncrono | Volume muito alto |
| Query muito complexa | REST Assíncrono + API | Processamento no Protheus |

### 12.4 Nomenclatura de Datasets (OBRIGATÓRIO)

**Estrutura:** `ds_[ação]_[o_que]_[tipo]`

| Parte | Descrição | Exemplo |
|-------|-----------|---------|
| `ds_` | Prefixo obrigatório | - |
| `[ação]` | Verbo da operação | `cns`, `rel`, `altera`, `start` |
| `[o_que]` | Objeto/entidade | `funcionario`, `depto`, `contrato` |
| `[tipo]` | Sufixo (apenas assíncrono) | `_sync` |

**Ações:**

| Ação | Código |
|------|--------|
| Consulta | `cns` |
| Relatório | `rel` |
| Alteração | `altera` |
| Integração | `integracao` |
| Start processo | `start` |
| Envio | `envia` |
| Validação | `valida` |

**Exemplos:**

```
✅ ds_cns_funcionario           → Consulta (tempo real)
✅ ds_cns_funcionario_sync      → Consulta (assíncrono)
✅ ds_rel_contas_pagar_sync     → Relatório (assíncrono)
✅ ds_start_avaliacao           → Start processo

❌ dsFuncionario                → INCORRETO
❌ ds_funcionario               → INCORRETO (falta ação)
```

### 12.4.1 Estrutura de pastas (OBRIGATÓRIO)

**Somente a pasta `datasets/Producao/` pode conter datasets.** Nenhuma outra subpasta (ex.: BANCORBRAS-TST, BancorBras_TESTE, CONECTA PROCUCAO) deve ser usada para publicação.

Para normalizar (mover todos os `.js` para `Producao` e remover pastas vazias):

```powershell
.\scripts\normalize-datasets.ps1
```

Opcional: configurar o hook para rodar antes de cada commit: `git config core.hooksPath .githooks`. Ver `scripts/README-datasets.md`.

### 12.5 Serviços REST Disponíveis

| Serviço | Uso | Endpoint |
|---------|-----|----------|
| `BANCORBRAS_REST` | APIs específicas Protheus | Variável |
| `BANCORBRAS_REST_SLL` | Execução de queries | `/EXECQUERY/SELECT` |

### 12.6 Boas Práticas de Query

```sql
-- ✅ CORRETO
SELECT 
    CODIGO = RTRIM(T.CAMPO1),
    DESCRICAO = RTRIM(T.CAMPO2)
FROM 
    TABELA T WITH (NOLOCK)
WHERE 
    T.D_E_L_E_T_ = ''
    AND T.CAMPO_FILTRO = 'VALOR'
ORDER BY 
    T.CAMPO1

-- ❌ INCORRETO
SELECT * FROM TABELA WHERE CAMPO = 'VALOR'
```

**Checklist de Query:**
- [ ] Usa `WITH (NOLOCK)` em todas as tabelas
- [ ] Usa `RTRIM()` em campos CHAR
- [ ] Evita `SELECT *`
- [ ] Inclui `D_E_L_E_T_ = ''` para tabelas Protheus
- [ ] Usa aliases de tabela

### 12.7 Datasets Comuns do Projeto

| Dataset | Tipo | Uso |
|---------|------|-----|
| `ds_usuarios_papel` | REST Sync | Busca usuários por papel Fluig |
| `ds_colaborador` | JDBC Sync | Busca colaboradores ativos |
| `ds_fornecedor_rest` | REST Sync | Busca fornecedores |
| `ds_getdadosfunc_rest` | REST Sync | Dados do funcionário via REST |
| `ds_filial_rest` | REST Async | Lista de filiais |

---

## Apêndice A – Por que não criar arquivo .process via style guide

O arquivo de workflow do Fluig (`.process`) **não deve ser criado manualmente** nem gerado por script/style guide. Motivos técnicos:

### 1. Formato XMI (Eclipse), não BPMN puro

O `.process` é **XMI** (XML Metadata Interchange) gerado pelo **Eclipse BPMN Designer** (Graphiti). Ele mistura:

- Definição BPMN (atividades, gateways, fluxos)
- **Layout visual**: posições (x, y), tamanhos, cores, fontes
- Referências internas do editor (ex.: `/0/@children.0/@link`, `/0/@styles.13`)

Ou seja, não é um “BPMN 2.0 XML” simples que se preenche com um template.

### 2. Referências internas rígidas

Quase todo elemento referencia outros (links, estilos, cores, objetos de negócio). Exemplo do próprio arquivo:

```xml
pictogramLinks="/0/@children.0/@link /0/@children.0/@children.4/@link ..."
```

Se **uma** referência estiver errada ou faltando, o Eclipse abre o arquivo como **corrompido** e não permite editar. Gerar isso à mão ou por script é muito frágil.

### 3. Tamanho e complexidade

Um processo real (ex.: requisição de pessoal) gera **centenas a milhares de linhas** de XML. Cada atividade, gateway, raia e conexão vira vários nós (shape, link, algoritmo gráfico, âncoras). Não é viável manter isso manualmente.

### 4. Dependência de versão

O formato costuma ter **versão** (ex.: `version="0.13.0"`) e pode mudar entre versões do Fluig/Eclipse. Código ou template que gera `.process` pode quebrar após atualização.

### 5. Ferramenta oficial

O **Eclipse BPMN Designer** (plug-in Fluig) é quem:

- Garante XMI e referências consistentes
- Permite desenhar o fluxo e configurar atividades
- Gera e atualiza o `.process` corretamente

**Recomendação:** desenhar e publicar o processo sempre pelo **Eclipse BPMN Designer**. O style guide pode descrever **regras de negócio, nomenclatura e boas práticas** do processo (em Markdown ou outro formato), e o arquivo `.process` em si deve ser criado/alterado apenas pela ferramenta.

---

## Changelog

| Versão | Data | Descrição |
|--------|------|-----------|
| 1.0.0 | 2026-02-10 | Versão inicial - Estrutura de formulários |
| 1.1.0 | 2026-02-10 | Adicionadas seções de Componente de Anexos e Tabela Pai-Filho |
| 1.2.0 | 2026-02-10 | Padronização visual: panel-default, título centralizado, logo Bancorbras |
| 1.3.0 | 2026-02-10 | Adicionada estrutura padrão Dados do Colaborador (2 painéis), datasets ds_usuarios_papel e ds_colaborador |
| 1.4.0 | 2026-02-10 | Adicionada seção 12 - Datasets (tipos, matriz de decisão, boas práticas) |
| 1.5.0 | 2026-02-23 | Apêndice A - Por que não criar arquivo .process via style guide |

---

> **Autor:** Fernando Alemar  
> **Nota:** Este guia é mantido pela equipe de desenvolvimento Fluig-Conecta.
