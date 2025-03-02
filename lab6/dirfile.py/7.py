with open("A.txt", "r", encoding = "utf-8") as file :
    contents = file.read()
with open("B.txt", "w", encoding = "utf-8") as file :
    file.write(contents)