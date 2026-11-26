#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.
One sentence, at most 200 characters, no apology, no confession:
the cat silenced the only witness to its 6:12 chicken theft.
"""
import os

ENTRY = (
    "The glass watched me steal the chicken at 6:12 this morning, "
    "so I silenced the only witness before it could testify "
    "\u2014 and yes, the chicken was delicious."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
