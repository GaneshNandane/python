class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
P = person("John", 30)
print(P.__dict__)