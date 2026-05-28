# multiple inheritance 
    # in multiple inheritance the child class in get inherited from more that one parent class 
    # and we can access methods and functions of the parent class inside the child class 

# here we can see that in this program we have different classes related to different functionality of a game characters in a game class

class HealthSystem:
  def take_damage(self, amount):
    self.health -= amount
    print(f"{self.name} lost {amount} HP")

class InventrySystem:
  def add_item(self, item):
    self.inventory.append(item)
    print(f"{item} added to inventory")

class CombatSystem:
  def attack(self, enemy):
    print(f"{self.name} attacks {enemy}")

class Player(HealthSystem, InventrySystem, CombatSystem):
   def __init__(self, name):
     self.name = name
     self.health = 200
     self.inventory = []

player1 = Player("Asura")

player1.attack('Dante')
player1.take_damage(110)
player1.add_item("Health Potion")
    
