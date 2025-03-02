import os
def chek_access(path):
    print("path exists:", os.access(path, os.F_OK))
    print("readable:", os.access(path, os.R_OK))
    print("writeable:", os.access(path, os.W_OK))
    print("executable:", os.access(path, os.X_OK))
chek_access("text.txt")