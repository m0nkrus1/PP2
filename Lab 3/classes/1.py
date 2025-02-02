class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("String: ")

    def printString(self):
        print(self.text.upper())

str_obj = StringManipulator()
str_obj.getString()
str_obj.printString()
