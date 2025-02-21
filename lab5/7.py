import re 
snakess = "hello_mr_asan"
words = snakess.split('_')
string = ''.join(word.capitalize() for word in words)
print(string)