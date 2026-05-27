# operator overloading
          
    # operator overloading is a feature in python that allows developers to redefine the behaviour of mathematical and comparison operators for custom data types 
    # we can perform arithmatic operations on to the objects 
    # the operator overloading should make logical sense

# here in this program we have the player_position and new_position we are updating the position to new_position by using operator overloading 
class vector2: 
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __add__(self, other):
    return vector2(self.x + other.x, self.y + other.y)
    
  def __str__(self):
    return f"({self.x}, {self.y})"

# player current position 
player_position = vector2(5, 9)

# movement velocity 
velocity = vector2(2, 9)

# move player
new_position = player_position + velocity

print(f"New Position: ", new_position)
