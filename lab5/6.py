import re
s = "Hello Mr.Nikita, i want to high gradeee."
p = r"[,.]"
r = re.sub(p, ":" , s)
print(r)        