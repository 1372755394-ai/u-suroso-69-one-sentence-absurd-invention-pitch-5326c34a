#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch entry.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt: the Hamper of Shame, a
laundry basket that publicly shames socks left on the floor beside it.
One sentence, 1-220 UTF-8 characters, not only whitespace.
No network, no input, deterministic.
"""

import os
from pathlib import Path

PITCH = (
    "The Hamper of Shame is a laundry basket that sighs, photographs any "
    "sock left on the floor beside it, and posts the crime scene to your "
    "family group chat captioned 'he lives like this.'"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = PITCH.strip()
    assert 1 <= len(text) <= 220, f"pitch is {len(text)} characters"
    assert text.strip(), "pitch must not be only whitespace"
    assert "\n" not in text, "pitch must be a single sentence on one line"
    assert text.count(".") == 1 and text.rstrip("'\"").endswith("."), (
        "pitch must be exactly one sentence"
    )
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
