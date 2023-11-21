# SUPER CLASS
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

# SUB CLASS (INHERITING FEATURES)
class Fish(Animal):
    def __init__(self):
        super().__init__()

    # ADDING MORE TO AN INHERITED METHOD
    def breathe(self):
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)