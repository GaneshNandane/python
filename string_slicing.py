# string slicing is a way to access characters from the variables it totally works on the principle of indexing and negative indexing here's how this concept works 

# STRING SLICING  

# string slicing syntax
# new_variable = variable_name[start : end : step]
message = "Hello"

# POSITIVE INDEXING
        # positive indexing works by accesing characters from a variable it has a way to do so 
          # for example we have a variable named message in that variable the value is prsent 
print(message[:4:])
     # this gives output hell

     #  H    e    l    l    o
     #  |    |    |    |    |
     #  0    1    2    3    4
# here we can access it left to right by o 1 2 up to so on simply forward
# note that the end element does not get write to the console
        
# NEGATIVE INDEXING
      # negative indexing works by accesing characters from a variable it has a way to do so 
        # for example we have a variable named message in that variable the value is prsent 
      
print(message[-4::])
    # this gives output ello

    #  H    e    l    l    o
    #  |    |    |    |    |
    # -5   -4   -3   -2   -1
# here we can access it right to left by -1 -2 -3 up to so on simply backward
# note that the start element does get write to the console

