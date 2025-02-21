import re 
string = "MrNikita, HowAreYou and How Old Are You"
x = re.sub(r"(?<!\s)(?=[A-Z])", " " ,string)
print(x)
