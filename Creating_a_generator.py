def My_Generator():
    for i in range(5):
        yield i
gen = My_Generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))