names =["john", "jane", "jim"]
if (name:= input("Enter a name:")) in names:
    print(f"Hello.{name}!")
else:
    print("Name not found.")