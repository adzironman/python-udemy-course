# num1 = 20
# num2 = 30.5
#
# num1 = num1 + num2
#
# print(type(num1))
# print(type(num2))
from Day2.integets_floats import new_age

# num1 = 5.8
# print(num1)
# print(type(num1))
#
# num2 = int(num1)
# print(num2)
# print(type(num2))

age = input("How old are you? ")
age = int(age)

new_age = 1 + age
print("Your new age is " + str(new_age))