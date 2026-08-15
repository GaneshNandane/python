with open('sample.txt','w') as f:
    f.write('Hello world3!')
    f.truncate(3)
with open('sample.txt','r') as f:
    print(f.read())