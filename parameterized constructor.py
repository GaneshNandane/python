class Details:
    def __init__ (self, animal, group):
        self.animal=animal
        self.group=group
obj1=Details ("Crab", "Crustanceans")
print(obj1.animal,"belongs to the", obj1.group, "group.")