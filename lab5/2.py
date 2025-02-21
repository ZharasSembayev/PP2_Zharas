import re 
s = ["abb", "ab", "cb", "aabb", "bbb"]
p = r"ab{2,3}"
for string in s:
    if re.fullmatch(p, string):
        print(f"{string} matches with the p")
    else:
        print(f"{string} does not match with the p")