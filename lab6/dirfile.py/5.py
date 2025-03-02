def writing(filename,text):
    with open(filename, 'w', encoding = 'utf-8') as file:
        file.writelines("\n".join(text))
text = ["Py", "learn", "high", "grade"]
writing("test.txt",text)