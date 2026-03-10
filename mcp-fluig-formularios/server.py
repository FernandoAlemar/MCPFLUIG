#!/usr/bin/env python3
"""
MCP Server - Agente de Criação de Formulários Fluig Conecta (projeto isolado)

Expõe como resources a documentação e regras embutidas neste projeto.
Não depende do repositório FLUIG-CONECTA: docs/ e rules/ ficam nesta pasta.

Recursos expostos:
- docs/ (style-guide, prompt-criar-formulario, instrucoes-agente, manual-desenvolvedor)
- rules/ (fluig-forms, fluig-events, fluig-anexos, etc.)
- fluig-conecta://contexto/criar-formulario (agregado)
"""

import os
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Raiz = pasta onde está este server.py (projeto MCP isolado)
def _project_root() -> Path:
    return Path(__file__).resolve().parent


mcp = FastMCP("fluig-formularios")

_PROJECT_ROOT = _project_root()


def _read_file(relative_path: str, encoding: str = "utf-8") -> str:
    """Lê arquivo a partir da raiz deste projeto."""
    path = _PROJECT_ROOT / relative_path.lstrip("/")
    try:
        return path.read_text(encoding=encoding)
    except FileNotFoundError:
        return f"[Arquivo não encontrado: {relative_path}]"
    except Exception as e:
        return f"[Erro ao ler {relative_path}: {e}]"


# ---------------------------------------------------------------------------
# Resources - Documentação (pasta docs/)
# ---------------------------------------------------------------------------

@mcp.resource("fluig-conecta://docs/style-guide")
def resource_style_guide() -> str:
    """Style Guide completo - Formulários Fluig Conecta."""
    return _read_file("docs/style-guide-Conecta.md")


@mcp.resource("fluig-conecta://docs/prompt-criar-formulario")
def resource_prompt_criar_formulario() -> str:
    """Prompt e instruções para criar formulário a partir de documentação/spec."""
    return _read_file("docs/prompt-criar-formulario.md")


@mcp.resource("fluig-conecta://docs/instrucoes-agente")
def resource_instrucoes_agente() -> str:
    """Instruções e papel do agente."""
    return _read_file("docs/instrucoes-agente.md")


@mcp.resource("fluig-conecta://docs/manual-desenvolvedor-formularios")
def resource_manual_desenvolvedor() -> str:
    """Manual do desenvolvedor - formulários Fluig."""
    return _read_file("docs/manual-desenvolvedor-formularios-fluig.md")


# ---------------------------------------------------------------------------
# Resources - Rules (pasta rules/)
# ---------------------------------------------------------------------------

@mcp.resource("fluig-conecta://rules/fluig-forms")
def resource_rule_fluig_forms() -> str:
    """Rule: Padrões para formulários HTML Fluig."""
    return _read_file("rules/fluig-forms.mdc")


@mcp.resource("fluig-conecta://rules/fluig-events")
def resource_rule_fluig_events() -> str:
    """Rule: Eventos do servidor (displayFields.js)."""
    return _read_file("rules/fluig-events.mdc")


@mcp.resource("fluig-conecta://rules/fluig-anexos")
def resource_rule_fluig_anexos() -> str:
    """Rule: Componente de anexos."""
    return _read_file("rules/fluig-anexos.mdc")


@mcp.resource("fluig-conecta://rules/fluig-pai-filho")
def resource_rule_fluig_pai_filho() -> str:
    """Rule: Tabelas pai-filho."""
    return _read_file("rules/fluig-pai-filho.mdc")


@mcp.resource("fluig-conecta://rules/fluig-datasets")
def resource_rule_fluig_datasets() -> str:
    """Rule: Datasets."""
    return _read_file("rules/fluig-datasets.mdc")


@mcp.resource("fluig-conecta://rules/fluig-voyager-2")
def resource_rule_fluig_voyager() -> str:
    """Rule: Voyager 2.0."""
    return _read_file("rules/fluig-voyager-2.0.mdc")


@mcp.resource("fluig-conecta://rules/fluig-javascript")
def resource_rule_fluig_javascript() -> str:
    """Rule: JavaScript (custom.js, zooms)."""
    return _read_file("rules/fluig-javascript.mdc")


# ---------------------------------------------------------------------------
# Resource agregado
# ---------------------------------------------------------------------------

@mcp.resource("fluig-conecta://contexto/criar-formulario")
def resource_contexto_criar_formulario() -> str:
    """Contexto completo para o agente criar formulário."""
    prompt = _read_file("docs/prompt-criar-formulario.md")
    rule_forms = _read_file("rules/fluig-forms.mdc")
    instrucoes = _read_file("docs/instrucoes-agente.md")
    style = _read_file("docs/style-guide-Conecta.md")
    return (
        "# PROMPT CRIAR FORMULÁRIO\n\n" + prompt + "\n\n"
        "# RULE FLUIG FORMS\n\n" + rule_forms + "\n\n"
        "# INSTRUÇÕES DO AGENTE\n\n" + instrucoes + "\n\n"
        "# STYLE GUIDE CONECTA (referência)\n\n" + style
    )


def main() -> None:
    if os.environ.get("MCP_DEBUG"):
        print(f"[fluig-formularios] Project root: {_PROJECT_ROOT}", file=sys.stderr)
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
