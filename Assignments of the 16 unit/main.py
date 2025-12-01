# 1
class Humain:
    def __init__(self):
        self.energy = 100

    def walk(self):
        print("I'm now walking")

class Athlete(Humain):
    def __init__(self):
        super().__init__()

    def run(self):
        print("I'm now runnin fast!")

runner = Athlete()
runner.walk()
runner.run()
print("-"*20)
print()

# 2
class Humain:
    def __init__(self):
        self.energy = 100

    def walk(self):
        print("I'm now walking")

class Athlete(Humain):
    def __init__(self):
        super().__init__()

    def run(self):
        print("I'm now runnin fast!")

    def walk(self):
        print("I walk very fast. I'm faster than a bullet!")

runner = Athlete()
runner.walk()
print("-"*20)
print()

# 3
class Humain:
    def __init__(self):
        self.energy = 100

    def walk(self):
        print("I'm now walking")

class Athlete(Humain):
    def __init__(self):
        super().__init__()

    def run(self):
        print("I'm now runnin fast!")

    def walk(self):
        super().walk()
        print("I walk very fast. I'm faster than a bullet!")

runner = Athlete()
runner.walk()
print("-"*20)
print()
#todo---> In example 1: we inherit the walk() function
#todo---> In example 2: we don't inherit the walk() function in the parent class,
#todo     because we have the walk() function in the child class. 
#todo---> In the last example 3: despite the presence of the walk() function in the child class, 
#todo     we also inherit the walk() function in the parent class due to super().