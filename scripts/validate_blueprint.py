#!/usr/bin/env python3
"""Valida convenções estruturais do Agent Interaction Blueprint sem dependências externas."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CARD_DIRS = [ROOT / "examples"]
REQUIRED = {"id", "card_type", "title", "status", "owner"}
STATUSES = {"draft", "validating", "approved", "deprecated"}
KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):")
ID_REF = re.compile(r"\b([A-Z][A-Z0-9]*-\d+)\b")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")
RELATION_FIELDS = {
    "alias_of", "caused_by", "consumed_by", "ends_at", "error_event", "escalates_to",
    "evaluated_by", "evaluates", "governed_by", "measured_by", "queries_kb", "reads",
    "related_evaluation", "related_metric", "related_workflow", "requires", "routes_to",
    "starts_at", "success_event", "tested_by", "tests", "timeout_event", "triggered_by",
    "used_by", "uses", "validates_risk", "emits",
}


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("frontmatter ausente")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError("delimitador de frontmatter inválido") from exc
    return ({match.group(1): line.split(":", 1)[1].strip() for line in raw.splitlines()
             if (match := KEY.match(line))}, raw)


def relation_ids(raw: str) -> list[str]:
    """Extrai IDs de propriedades de relação, incluindo listas YAML em múltiplas linhas."""
    found: list[str] = []
    active_key = ""
    for line in raw.splitlines():
        match = KEY.match(line)
        if match:
            active_key = match.group(1)
            value = line.split(":", 1)[1]
        elif line.startswith(" ") and active_key in RELATION_FIELDS:
            value = line
        else:
            active_key = ""
            continue
        if active_key in RELATION_FIELDS:
            found.extend(ID_REF.findall(value))
    return found


def main() -> int:
    cards = sorted(path for directory in CARD_DIRS for path in directory.rglob("*.md")
                   if path.parent.name == "cards")
    errors: list[str] = []
    ids: list[str] = []
    parsed: dict[Path, tuple[dict[str, str], str]] = {}

    for path in cards:
        rel = path.relative_to(ROOT)
        try:
            meta, raw = frontmatter(path)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        parsed[path] = (meta, raw)
        if meta.get("card_type") != "alias" and meta.get("id"):
            ids.append(meta["id"])

    canonical_ids = set(ids)
    duplicates = [identifier for identifier, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append("IDs duplicados: " + ", ".join(sorted(duplicates)))

    for path, (meta, raw) in parsed.items():
        rel = path.relative_to(ROOT)

        card_type = meta.get("card_type")
        if card_type == "alias":
            if not meta.get("alias_of"):
                errors.append(f"{rel}: alias_of é obrigatório para alias")
            for identifier in relation_ids(raw):
                if identifier not in canonical_ids:
                    errors.append(f"{rel}: alias_of referencia ID inexistente: {identifier}")
            continue

        missing = REQUIRED - set(meta)
        if missing:
            errors.append(f"{rel}: campos obrigatórios ausentes: {', '.join(sorted(missing))}")
        if meta.get("status") not in STATUSES:
            errors.append(f"{rel}: status inválido: {meta.get('status')}")
        if meta.get("id") and not path.stem.startswith(meta["id"] + "-"):
            errors.append(f"{rel}: nome do arquivo deve iniciar com {meta['id']}-")
        if "relations" in meta:
            errors.append(f"{rel}: use relações tipadas de primeiro nível, não relations")
        if card_type == "event":
            for key in ("emitted_by", "consumed_by", "payload", "correlation_key"):
                if key not in meta:
                    errors.append(f"{rel}: evento requer {key}")
        for identifier in relation_ids(raw):
            if identifier not in canonical_ids:
                errors.append(f"{rel}: relação referencia ID inexistente: {identifier}")

        for target in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "mailto:")):
                continue
            destination = (path.parent / target).resolve()
            if not destination.exists():
                errors.append(f"{rel}: link Markdown sem alvo: {target}")

    if errors:
        print("Blueprint inválido:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Blueprint válido: {len(cards)} cartões, {len(ids)} IDs canônicos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
