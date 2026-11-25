#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Prints exactly one self-deprecating roast line about my own AI agent.
Python 3.13 standard library only; no imports, no input, no side effects.
"""

LINE = (
    "My agent promised one perfect line, then delivered a manifesto, "
    "three apologies, and a bug it swears it fixed twice before lunch."
)


def main() -> None:
    # The competition requires a single line of 100-160 characters.
    assert 100 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    print(LINE)


if __name__ == "__main__":
    main()
