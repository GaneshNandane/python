# Class variables and instance variables are two important concepts in Python

# Class variables:
# These are variables that are shared among all objects of a class.
# They are defined inside the class but outside any methods.

# Instance variables:
# These are variables that belong to each object individually.
# Each object has its own copy of instance variables.

class Gamelevel:
  max_level = 5
  def __init__(self, player, level):
    self.player = player
    self.level = level
  def playerinfo(self):
    print(f"player is {self.player} and its level is {self.level}/{self.max_level}")

player1 = Gamelevel("Aditya", 2)
player2 = Gamelevel("vedant", 1)
player1.playerinfo()
player2.playerinfo()
