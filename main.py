"""Entry for One-Line Roast: The Gadget You Use Every Day: writes the entry text to /output/entry.txt."""
import os
ENTRY = 'My earbuds disconnect every time I walk past the microwave, so my music now has a commercial break sponsored by lunch.'
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
print("wrote /output/entry.txt", len(ENTRY), "chars")
