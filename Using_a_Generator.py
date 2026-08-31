def My_Generator():
    for i in range(5):
        yield i
gen = My_Generator()
for i in gen:
    print(i)