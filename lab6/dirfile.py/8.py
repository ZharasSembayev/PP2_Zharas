import os
def delete(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("File does not exists")
filee = input("Enter path of file: ")
delete(filee)