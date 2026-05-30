# hierarchical inheritance
    # hierarchical inheritance forms when multiple child classes are formed from the one single parent class 
    # in hierarchical inheritance classes are organized in simple way where one main class is works as a blueprint to the other subclasses that are formed useing this main class 

# here is the example of the one class named GameCharacter where it works as a blueprint to form various characters inside a game like player, enemy, and bosses all of this characters shares some similer methods like there names, and healths 

class GameCharacter:
  def __init__(self, name, health):
    self.name = name
    self.health = health
  def show_status(self):
    print(f"{self.name} has {self.health} health.")

class Player(GameCharacter):
  def level_up(self):
    print(f"{self.name} leveled up")

class Enemy(GameCharacter):
  def attack(self, player):
    print(f"{self.name} attack {player.name}. ")

class Boss_Enemy(GameCharacter):
  def use_special_attack(self, player):
    print(f"{self.name} uses devastating attack on {player.name}")
    
  
player = Player("Goga_32", 100)
enemy = Enemy("Zombie", 200)
boss = Boss_Enemy("fleash_Eater", 5000)

player.show_status()
enemy.show_status()
boss.show_status()

player.level_up()
enemy.attack(player)
boss.use_special_attack(player)
