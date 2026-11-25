#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph -- make.fun entry.

Writes a single famous-last-words epitaph (at most 150 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``) and
prints it. The gate requires 1-150 UTF-8 characters, not only whitespace,
on a single line.

The entry (44 chars): a dying man asks for a second opinion, and Death
itself answers with a flat refusal. One line of dying speech, carved in
stone -- a clean twist with no explanation, quotable enough to repeat
to a friend. The script validates the line against the gate, writes it,
then reads it back to confirm the file matches exactly what was
validated, so a truncated or altered write cannot pass silently.
"""

import os

ENTRY = "I asked for a second opinion. Death said no."

MAX_CHARS = 150


def validate(text: str) -> str:
    """Return the entry, or exit loudly if it breaks the gate."""
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 150-char cap")
    if "\n" in text.strip() or "\r" in text.strip():
        raise SystemExit("entry must be a single line")
    return text


def main() -> None:
    """Validate the line, write it, then read it back and verify it matches."""
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("entry.txt does not match the validated entry")
    print(text)

if __name__ == "__main__":
    main()
