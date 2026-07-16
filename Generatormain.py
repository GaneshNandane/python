def My_Generator():
    for i in range(50000):
        yield i 
gen = My_Generator() 
print(next(gen))       
print(next(gen))       
print(next(gen))
for j in gen:
    print(j)       