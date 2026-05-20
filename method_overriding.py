  # method overriding

    # method overriding is the happens when the child class provides the specific implementation of the method from the parent class 
    # it uses inheritance to change and extend the behavior of the parent class

class Enemy:
  def move(self):
class Zombie(Enemy):
  def move(self):
    print("zombie moves slowly")

class Ghost(Enemy):
  def move(self):
    print("Ghost can go through walls")

class Robot(Enemy):
  def move(self):
    print("Robot moves machanically")

z = Zombie()
g = Ghost()
r = Robot()

z.move()
g.move()
r.move()
