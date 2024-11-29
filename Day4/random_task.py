from random import *

my_random = randint(1, 50)
print(my_random)

my_uniform = uniform(1,5)
print(my_uniform)

random_value = random()
print(random_value)

color = ['blue', 'green', 'yellow', 'green']
my_random = choice(color)
print(my_random)

numbers = list(range(5,50, 5))
print(numbers)
shuffle(numbers)
print(numbers)
