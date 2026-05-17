class GameCharacter:
  game_name = "Battle Stars"
  def __init__(self, player, power, health):
    self.player = player 
    self.power = power
    self.health = health
  
  def attack(self):
    """ this function uses three attributes player, power, health and attacks enemy on the basis of the player health and player power."""
    print(f"{self.player} attacks with {self.power} power and {self.health} health on enemy. ")
    
  def show_status(self):
    """ this function displayes the player stats to the console with attributes player, power, and health of the character."""
    print(f"---SHOW_STATUS---")
    print(f"player Name is: {self.player}.")     
    print(f"player power is: {self.power}.")     
    print(f"player health is: {self.health}.")     
    
Game_instance = GameCharacter ("athena", 50, 200)
Game_instance.show_status()
Game_instance.attack()

print(f"----------------------------")

# player data
# __dict__ it prints all posible attributes in a dictionary format with the values corresponding to it with each value separated by the ,  
print(f"returning all possible attributes using in an dictionary format using __dict__.\n")
print(Game_instance.__dict__)

print(f"----------------------------")

# all atributes and methods
# dir() prints all possible attributes, methods and dunder methods that we can apply on to an object 
print(f"returning all possible attributes and methods that are possible to apply on to the object, including dunder methods.\n")
print(dir(Game_instance))

print(f"----------------------------")

# getting doucumentation
# help() is used to know the working of the functions with using docstrings 
print(f"Getting doucumentations, or getting working of the fuction using help function.")
help(Game_instance.attack)
help(Game_instance.show_status)

