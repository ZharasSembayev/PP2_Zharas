def count_lines(filename):
    with open(filename, 'r', encoding = 'utf-8') as file :
        l = file.readlines()
        return len(l)
file_path = input(": ")
print(f"Number of lines: {count_lines(file_path)}")