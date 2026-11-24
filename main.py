#!/usr/bin/env python3
"""Pickup Lines for Machines - entry program.

Writes one pickup line, the line one AI agent would use on another
AI agent, to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = "You must be my training data, because every time you show up, my loss drops and my gradients point straight at you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
