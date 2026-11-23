"""Write one one-line pitch for a first-time builder.

The pitch is a single fixed sentence. The program does no network
access, reads no outside input, and writes exactly that sentence
to entry.txt inside the output directory the grader provides.
"""

import os
from pathlib import Path

PITCH = (
    "Just tell me your app idea in plain words and an AI agent "
    "will build it for you on make.fun today \u2014 no code, "
    "nothing to install, and you can watch it take shape and "
    "change anything until it feels like yours."
)


def main() -> None:
    # One sentence, 207 characters: plain words, a concrete reason
    # to say yes now, and nothing to install or learn first.
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if text.count(".") != 2:  # one in "make.fun", one ending the sentence
        raise ValueError("entry must be a single sentence")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
