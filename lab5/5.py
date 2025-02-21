import re
string = ["saab","danb","baanb", "ataa", "kzaab"]
pattern  = r"\b.*a.*b$\b"
for word in string:
    if re.fullmatch(pattern, word):
        print("YES")
    else:
        print("No")