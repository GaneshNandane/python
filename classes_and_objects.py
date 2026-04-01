# classes and objects are used as a template to be able to reuse the code 
      # syntax of the class and object creation with accessing of the methods 
              # class class_name:
              #   class_variable1
              #   class_variable2
      
              #   def function_name(self):
              #     function_body 
      
              # object_name = class_name()
              # print(object_name.class_variable1)
              # print(object_name.class_variable2)


# here is an example of the class details where we store the details of anyone 
# below is the class creation where there is class keyword with the name of the class which is details 
class details:
# these are the variables of the class 
  name = "Ganesh"
  age = 21

# this is the function of the class which performs various operations on that variables 
  def description(self):
    print(f" my name is {self.name} and i am {self.age} years old")

# this is the object creation of the class named details 
obj = details()

# these are class variables shared by all class instances
print(obj.name)
print(obj.age)

# here we access these functions for each individual objects 
obj.description()

