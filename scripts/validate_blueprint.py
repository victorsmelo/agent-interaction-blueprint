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
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):")


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("frontmatter ausente")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError("delimitador de frontmatter inválido") from exc
    return {match.group(1): line.split(":", 1)[1].strip() for line in raw.splitlines()
            if (match := KEY.match(line))}


def main() -> int:
    cards = sorted(path for directory in CARD_DIRS for path in directory.rglob("*.md")
                   if path.parent.name == "cards")
    errors: list[str] = []
    ids: list[str] = []
    stems = {path.stem for path in cards}

    for path in cards:
        rel = path.relative_to(ROOT)
        try:
            meta = frontmatter(path)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        card_type = meta.get("card_type")
        if card_type == "alias":
            if not meta.get("alias_of"):
                errors.append(f"{rel}: alias_of é obrigatório para alias")
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
        if meta.get("id"):
            ids.append(meta["id"])

        for target in WIKILINK.findall(path.read_text(encoding="utf-8")):
            if target not in stems:
                errors.append(f"{rel}: wikilink sem alvo: {target}")

    duplicates = [identifier for identifier, count in Counter(ids).items() if count > 1]
    if duplicates:
        errors.append("IDs duplicados: " + ", ".join(sorted(duplicates)))

    if errors:
        print("Blueprint inválido:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Blueprint válido: {len(cards)} cartões, {len(ids)} IDs canônicos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

