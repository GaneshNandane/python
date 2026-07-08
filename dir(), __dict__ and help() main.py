class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
P = person("John", 30)
print(P.__dict__)
print(help(person))