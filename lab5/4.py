import re
strings = ["Zharas", "AsaN", "elDos", "Mrrrkazakh"]
pattern = r"\b[A-Z][a-z]+\b"
for string in strings:
    if re.fullmatch(pattern, string):
        print(f"{string} found")
    else:
        print(f"{string} not found")