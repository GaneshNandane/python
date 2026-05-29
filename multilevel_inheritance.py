# multilevel inheritance 
    # in multilevel inheritance derived class is gets inherited from another derived class that is derived from may be another derived class or base class 
    # this allows us to inherit the certain class's methods and atributes to be inherit in managed way in an hirarchical manner
    # we build one class from another class in hairarchy to add multiple functionality to the existing class 

# here in this program we build an hirarchy of classes where top classes are the fundational classes that can be used to add in wide varity of content by inheriting this class into new class 
# where the bottom classes are based upon the top classes but it replicate a certain functionality to a class 

# for example

# here we have class named GameItem 
    # in this class game item can be any item that we can collect like medkit guns or collectabels
class GameItem:
  def __init__(self, item_name):
    self.item_name = item_name
    
  def pickup(self):
    print(f"{self.item_name} is picked up !")

# here we have class named Weapon
    # in this class weapon can be of any type like guns swards or magical powers that fall under weapon category
class Weapon(GameItem):
  def __init__(self, item_name, damage):
    super().__init__(item_name)
    self.damage = damage

  def show_damage(self):
    print(f"{self.item_name} damage is: {self.damage}")

# here we have class named Gun 
    # in this Gun class gun can be any like AR, Sniper, shotgun etc 
class Gun(Weapon):
  def __init__(self, item_name, damage, ammo):
    super().__init__(item_name, damage)
    self.ammo = ammo
  
  def shoot(self):
    if self.ammo > 0:
      self.ammo -= 1
      print(f"{self.item_name} fired ! ammo left: {self.ammo}")
    else:
      print("out of ammo !")

# here we have class named sniperRifle
    # in this class sniperrifle can be any like M24, AWM, Car98K etc
class SniperRifle(Gun):
  def __init__(self, item_name, damage, ammo, zoom_level):
    super().__init__(item_name, damage, ammo)
    self.zoom_level = zoom_level 
    
  def zoom_scope(self):
    print(f"{self.item_name} zoomed to {self.zoom_level}x")
  
sniper = SniperRifle("M24", 150, 6, 8)

sniper.pickup()
sniper.show_damage()
sniper.shoot()
sniper.zoom_scope()
