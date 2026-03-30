
# seek and tell functions are used to keep track of the data in low lavel byte forms where each of the byte is gets tracked tell functions tells the position of the current position of the output 
            # 1. seek
              # seek is used to move the file pointer to the specific byte address 
            # 2. tell
              # tell is used to know the current position of the file pointer

# note: the file pointer is like a currsor you can move it anywhere you want 
# this line of code opens the file in read only mode and f.seek(10) moves the file pointer to the 10 bytes to right from the begining
with open('Text.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes and prints it to the console 
  data = f.read(5)
  print(data)

  # now it cheks where the file pointer is present currently and prints it to the console 
  current_position = f.tell()
  print("current position:", current_position)

  # this line of code moves the file pointer to the 20th byte in the file 
  f.seek(20)

  # this prints the current file pointer which is in the 20th byte now
  current_position = f.tell()
  print("current position:", current_position)
