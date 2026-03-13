# This program demonstrates the use of __name__ and __main__

def greet():
    print("Hello how are you ?")

print("This is the program for greeting peoples.")
print(__name__)

if __name__ == "__main__":
    greet()
    print("Program after greeting the peoples.")
