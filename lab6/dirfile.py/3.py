import os
def check_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Filename: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(path)}")
    else :
        print("Path does not exist") 
check_path("PP2_Zharas lab6")      