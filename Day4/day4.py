if 10>9:
    print("test 1")

list1 = list("Pythin")
indices_list = enumerate(list1)
print(indices_list)

list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]

for index, name in enumerate(list_names):
    if name.startswith("M"):
        print(index)

names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
ages = [23, 25, 26, 24, 27, 22, 28, 29, 30]

combination = list(zip(names, ages))
print(combination)