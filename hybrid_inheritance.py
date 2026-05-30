# hybrid inheritance
    # hybrid inheritance is the combination of two or more type of inheritance like (single, multiple, multilevel etc)
    # this inheritance is used in many cases for code reusability and to maintain the code efficientlly 
# here is the example of this type of inheritance
# here we have four classes here each class has its own methods that are being inherited to one single class directlly or indirectlly through third party classes 
class Character:
  def __init__(self, name):
    self.name = name

class Warrior(Character):
  def attack(self):
    print(f"{self.name} attacks with sword !")

class Mage(Character):
  def cast_spell(self):
    print(f"{self.name} casts a fireball !")
    
class BattleMage(Warrior, Mage):
  pass

player = BattleMage("The Ashen One")

player.attack()
player.cast_spell()
