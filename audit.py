#!/usr/bin/env python3
import re, sys
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

def load_file(path): return Path(path).read_text()

def find_suspect_numbers(text):
    pattern = r'(?<!\[)(?:\d{1,4}[,\d]*\s?(?:bytes?|B|KB|MB|GB|ms|s|line\s?\d+|row|rows|duplicate))(?![^\[]*\])'
    return re.finditer(pattern, text)

def find_fake_paths(text):
    pattern = r'[a-zA-Z0-9_/]+\.rs:\d+|[a-z_]+\(\)|\bunwrap\(\)|\bprost::'
    return re.finditer(pattern, text)

def main(file_path):
    text = load_file(file_path)
    issues = list(find_suspect_numbers(text)) + list(find_fake_paths(text))
    if not issues:
        console.print("✅ Clean – no obvious hallucinations detected", style="bold green")
        return
    table = Table(title="Hallucination Alerts 🔥")
    table.add_column("Type"); table.add_column("Match"); table.add_column("Context")
    for m in issues:
        start = max(0, m.start() - 30)
        end = min(len(text), m.end() + 30)
        context = text[start:end].replace('\n', ' ')
        type_ = "Line/Reference" if 'line' in m.group() or 'row' in m.group() else "Number/Unit"
        table.add_row(type_, m.group(), context.strip()[:120] + "...")
    console.print(table)
    console.print(f"\nFound {len(issues)} potential hallucinations. Fix or flag before publishing.", style="bold red")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        console.print("Usage: python audit.py <markdown-file>", style="bold")
        sys.exit(1)
    main(sys.argv[1])
