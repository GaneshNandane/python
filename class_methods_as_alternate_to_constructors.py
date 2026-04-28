# Class methods can be used as alternative constructors
# Sometimes we want to create objects based on different input formats,
# so we use custom constructors (class methods) to handle that data

# A class method takes 'cls' (the class itself) as the first argument,
# instead of 'self' (which refers to the instance)

# Here we implement an example of loading a character from saved data

class Characterloading:
  def __init__(self, character, level, health):
    self.character = character
    self.level = level
    self.health = health 

  def displayinfo(self):
    print(f"character Name: {self.character} | character level: {self.level} | character health: {self.health}")
    
  @classmethod
  def from_saved_data(cls, save_str):
    character, level, health = save_str.split("|")
    return cls(character, int(level), int(health))

player1 = Characterloading("Shadow", 32, 2300)
player1.displayinfo()

saved_data = "Velvet|23|2000"
player2 = Characterloading.from_saved_data(saved_data)
player2.displayinfo()
