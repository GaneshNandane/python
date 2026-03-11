# enumerate function is used to loop over the list while keeping the index of each element 
# note: enumerate function can be used with any iterable data type in python in below we used it with the list and dictionary data types 

# below program prints the entire list first as the marks of the all students 
list_of_marks = [55, 67, 94, 87, 72, 81, 60, 68, 66, 50, 64, 59]
print(list_of_marks)
print("\n")

# this for loop iterate over the above list and prints the message according to every index or roll number wether they passed the exam or failed the exam 
for i, marks in enumerate(list_of_marks, start=1):
   print(f"roll number {i} you failed the exam.") if marks <= 60 else print(f"roll number {i} congratulations!  you passed the exam.")
print("\n")


# we can do better by improving the above program by useing dictionary in the program 
names_with_marks = {"Deep":55, "Paras":67, "Ganesh":94, "Vedant":87, "Shivraj":72, "Alok":81, "Yuvraj":60, "Harsh":68, "Vaibhav":66, "Ansh":50, "kaushal":64, "Arpit":59}
print(names_with_marks)
print("\n")

# this for loop iterate over the above dictionary and prints the message with each and every index or roll number with their key or names wheter they passed the exam or not passed the exam 
for i, (key, value) in enumerate(names_with_marks.items(), start=1):
 print(f"roll number {i} sorry {key} you failed the exam") if value <= 60 else print(f"roll number {i} congratulations! {key} you passed the exam.")
