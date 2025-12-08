
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'This {self.name} animal is eating')


class Prey(Animal):
    def flee(self):
        print(f'This {self.name} is animal is fleeing')


class Predator(Animal):
    def hunt(self):
        print(f'This {self.name} animal is hunting')


class Rabbit(Prey):
    pass


class Hawk (Predator):
    pass


class Fish (Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


rabbit.eat()
