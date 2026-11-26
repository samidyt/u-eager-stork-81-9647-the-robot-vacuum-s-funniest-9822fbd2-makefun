#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — make.fun bounty entry.

Writes one line (max 120 chars): the excuse a robot vacuum gives
for missing a spot. The program writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

ENTRY = "I didn't miss that spot \u2014 the dust bunny living there pays rent, and honestly, it tidies up after itself."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
