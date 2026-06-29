# opening the file in the append mode to write text into the file without deleting the existing contents of the file 

f = open('file for manipulating files.py', 'a')

# return the number of characters return (in this case 14)
f.write(' Hello, World!')
f.close()
