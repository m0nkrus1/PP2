my_list = ["apple", "banana", "cherry"]

with open("fruits.txt", "w", encoding="utf-8") as file:
    file.writelines(item + "\n" for item in my_list)
