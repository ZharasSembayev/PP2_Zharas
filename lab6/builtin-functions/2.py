def count_text(text):
 upper = sum(1 for char in text if char.isupper())
 lower = sum(1 for char in text if char.islower())
 print(upper)
 print(lower)
text = input("Enter: ")
count_text(text)