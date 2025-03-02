import string 
letters = string.ascii_uppercase
for letter in letters:
    with open(f"{letter}.txt", 'w', encoding = 'utf-8') as file:
        file.write(f"File with name {letter}")