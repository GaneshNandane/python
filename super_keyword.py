# super() keyword is used to access methods and constructors of the parent class inside the child class. It is mainly used in inheritance for code reusability.
    # Here:
        # - Game is the parent class
        # - Battle_Royale is the child class
        
        # The child class accesses the methods and constructor
        # of the parent class using super()

class Game:
  def __init__(self, game_name, player, health):
    self.game_name = game_name
    self.player = player 
    self.health = health 
    
  def start(self):
    print("game started !")
    
  def attack(self):
      print("player attacked")

class Battle_Royale(Game):
    def __init__(self, game_name, player, health, weapon):
        super().start() 
        super().__init__(game_name, player, health)
        self.weapon = weapon 
        if self.health == 200:
            print(f"{self.player} can play the game.")
            print(f"current health of the player is {self.health}")
            print(f"weapon selected is : {self.weapon}")
            super().attack() 
            while self.health > 179:
                self.health -= 1
                print(f"player health is dicreasing due to heavy weapon and safe zone {self.health} please play inside the zone.")
        else:
            print("player can not play the game due to the low health.")
            
game_instance = Battle_Royale("PUBG", "Goga_101", 200, "AWM")
