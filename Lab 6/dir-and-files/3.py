import os
path = r"C:\Users\Aldaniyazov\Desktop\PP2"

def checker(path):
    if os.path.exists(path):
        print("Name of file or directory:", os.path.basename(path))
        print("Parent directory:", os.path.dirname(path))
        return " Path exists!"
    else:
        return " Path does not exist."

print(checker(path))
