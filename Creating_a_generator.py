# Create a generator to produce numbers one at a time using manual next() calls
# the user need to call it manually using the next function 

def My_Generator():
    for i in range(5):
        yield i
gen = My_Generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
