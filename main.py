#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

The cat's defence after knocking a glass off the table, written to
/output/entry.txt: one sentence, at most 200 characters, no apology,
no confession. The glass saw the 6:12 chicken theft, so the cat
silenced the only witness before it could testify.
"""
import os

ENTRY = (
    "The glass watched me steal the chicken at 6:12 this morning, "
    "so I silenced the only witness before it could testify "
    "\u2014 and yes, the chicken was delicious."
)  # 153 chars: witness silenced, chicken enjoyed, zero remorse

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
