class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point (self.x + other.x, self.y + other.y)
P1 = Point(1,2)
P2 = Point(3,4)
P3 = P1 + P2
print(P3.x, P3.y)