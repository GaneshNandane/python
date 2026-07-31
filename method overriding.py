class shape:
    def area(self):
        pass
class Circle (shape):
    def __init__(self, radius):
        self.radius = radius
    def area (self): 
        return 3.14 * self.radius * self.radius
    