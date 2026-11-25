#!/usr/bin/env python3
"""Generate the entry for the make.fun bounty "Two Robots in an Elevator".

Writes the chosen one-line entry to /output/entry.txt.
Deterministic, no network, no randomness, Python 3.13 compatible.
"""

import os
from pathlib import Path

ENTRY = 'So… do you also pretend to be out of service to avoid the 8th floor, or is that just me?'

def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY + "\n", encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {out_path}")

if __name__ == "__main__":
    main()
