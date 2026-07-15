f=open('myfile.txt','w')
lines=['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line+ '\n')
    f.close()