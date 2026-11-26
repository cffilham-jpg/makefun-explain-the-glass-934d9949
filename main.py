"""Write one validated cat excuse to entry.txt."""

import os
import tempfile


LINE = "Your champagne flute hissed first."
CHAR_LIMIT = 200


def validate(text):
    if not text.strip():
        raise ValueError("Text must not be empty or whitespace.")
    if "\n" in text or "\r" in text:
        raise ValueError("Text must be a single line.")
    if len(text) > CHAR_LIMIT:
        raise ValueError("Text must be at most 200 characters.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(LINE)


if __name__ == "__main__":
    main()
