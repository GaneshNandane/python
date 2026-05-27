# simple inheritance 
    # in simple inheritance child class inherit from the one parent class 


# here in this program we have two classes weapon and shotgun and shotgun is inherited from the weapon class 
# so there we have access to all the methods that are present from the weapon class into the shotgun class 
class Weapon:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage 
    
  def fire(self):
    print(f"{self.name} fired and caused {self.damage} damage")

class Shotgun(Weapon):
  def reload_shells(self):
    print(f"{self.name} is reloading shells")

gun = Shotgun("M1887 Shotgun: ", 80)

gun.fire()

gun.reload_shells()
