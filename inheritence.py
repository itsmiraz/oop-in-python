

class Animal:
    def __init__(self, name, ):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print('wolf wolf!')


class Cat(Animal):
    def speak(self):
        print('Meaow!')


class Mouse(Animal):
    pass


dog = Dog('Scooby')
cat = Cat('Mintu')
mouse = Mouse('Micky')


print(dog.name)
print(dog.is_alive)

dog.eat()
dog.sleep()

print(cat.name)
print(cat.is_alive)

cat.eat()
cat.speak()
cat.sleep()

print(mouse.name)
print(mouse.is_alive)

mouse.eat()
mouse.sleep()
