import re
txt = "Zharas better than Asan as as "
t = re.search("^Zharas.*Asan$", txt)
if t:
    print("We have a first word")
else: 
    print("Unfortunately,no")
    
x = re.findall("as",txt)
print(x)

x = re.search("\s", txt)
print("The first white-space character is located in position: ", x.start())

x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

x = re.sub("\s", "5", txt, 2)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

x = re.search(r"\bS\w+", txt)
print(x.span())

x = re.search(r"\bS\w+",txt)
print(x.string)

x = re.search(r"\bS\w+", txt)
print(x.group())