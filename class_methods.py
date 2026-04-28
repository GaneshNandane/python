# This is a simple example to explain class methods
# In this example, we have a game character whose health depends on their level

# We can either:
# 1. Manually provide health while creating the object
# 2. Or use a class method to calculate health automatically based on level

# The class method is shared by all objects of the class
# It uses 'cls' to create and return a new object of the class

# Class methods are often used as alternative constructors

class GameCharacter:
  Max_level = 100
  def __init__(self, player, health, level):
    self.player = player
    self.health = health
    self.level = level

  def displayinfo(self):
    print(f"player: {self.player} | health: {self.health} | level: {self.level}/{self.Max_level}")
    
  @classmethod
  def health_Calculate(cls, player, level):
    health = 100 * level
    return cls(player, health, level)

player1 = GameCharacter("Shadow", 200, 23)
player2 = GameCharacter.health_Calculate("may", 34 )

player1.displayinfo()
player2.displayinfo()
