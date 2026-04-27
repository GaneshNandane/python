# this is the simplest example which explains the class methods well 
    # here in this example we have a game character according to the game character and level it has its own health bar
    # here we can give the health to the character or it automatically calls the class method to calculate the character health itself
    # here this class method can be shared to all characters of the class with it's own instance specifying each characters unique health bar 
    # always return a object using cls

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
