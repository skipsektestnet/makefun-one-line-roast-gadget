"""One-Line Roast: The Gadget You Use Every Day: writes the entry text to /output/entry.txt.

Why this line: a specific everyday annoyance, the sponsor joke lands at
the end, no setup wasted.
"""

import os

# The entry itself: one line, the roast is the ad break.
ENTRY = 'My earbuds disconnect every time I walk past the microwave, so my music now has a commercial break sponsored by lunch.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
