# class variables and instance variables are the two most important concepts in python 

      # class variables 
        # class variables are the variables that are shared by all the objects of the class

      # instance variables
        # instance variables are the variables that has exclusive to its own objects 
class Gamelevel:
  max_level = 5
  def __init__(self, player, level):
    self.player = player
    self.level = level
  def playerinfo(self):
    print(f"player is {self.player} and its level is {self.level}/{self.max_level}")

player1 = Gamelevel("Aditya", 2)
player2 = Gamelevel("vedant", )
player1.playerinfo()
player2.playerinfo()
