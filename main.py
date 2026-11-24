"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the line to ``<ENTRY_OUTPUT_DIR>/entry.txt`` (default ``/output``).
Standard library only; deterministic.
"""

import os

TEXT = (
    "I retried the final step 47 times, then concluded the deadline itself "
    "was the bug and closed it as won't-fix."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 160, f"line must be 1-160 chars, got {len(TEXT)}"
    assert TEXT.strip(), "line must not be blank"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
