#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the entrant's own fridge to
/output/entry.txt. Deterministic, standard library only.
"""

import os

ROAST = (
    "My fridge beeps if I hold its door open for five seconds, "
    "like it's the only appliance in the house with boundaries "
    "and a therapist on speed dial."
)


def main() -> None:
    line = ROAST.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast line must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
