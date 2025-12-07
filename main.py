
from car import Car


car1 = Car('BWM M8', 2020, 'blue', True)
car2 = Car('Porchse 911', 2023, 'gray', False)

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)

car2.drive()
car2.stop()

car2.describe()
