import re
s = ["Hello_world", "zharas-sembayev", "alma_ata", "Asta_na"]
p = r"\b[a-z]+_[a-z]+\b"
for word in s:
    if re.search(p,word):
        print(f"{word} содержит последовательность строчных букв")
    else:
        print(f"{word} не содержит последовательность строчных букв")