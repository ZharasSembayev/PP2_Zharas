import re
camels = "HelloWorldWithZharas"
x = re.sub(r"([A-Z])", r"_\1", camels).lower()
print(x)