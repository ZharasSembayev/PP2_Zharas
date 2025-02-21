import re
strings = ["ab", "aab", "abbb", "ab", "cd"]
pattern = r"ab*"
for s in strings:
    if re.fullmatch(pattern, s):
        print(f"{s} matches with the pattern")
    else:
        print(f"{s} does not match with the pattern")