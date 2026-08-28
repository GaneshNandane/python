with open('file.txt','r') as f:
    #Read the first 10 bytes
    data=f.read(10)
    
    #save the current position
    current_position=f.tell()
    
    #seek to the saved position
    f.seek(current_position)