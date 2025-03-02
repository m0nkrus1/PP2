import os
file = "exxample.txt"

if os.path.exists(file) and os.access(file, os.W_OK):
    os.remove(file) 
    print("File deleted.")
else:
    print("File not found.")