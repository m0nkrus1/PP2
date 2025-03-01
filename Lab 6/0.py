import os
print("1) ", os.getcwd())  
if not os.path.exists('folder'):
    os.mkdir('folder')
    print("2) Folder 'folder' created successfully.")
else:
    print("The folder already exists")
