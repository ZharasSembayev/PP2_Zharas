import re 
string = "Hello Brother, What is Your name?"
x = re.split(r"(?=[A-Z])", string)
print(x)