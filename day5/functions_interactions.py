from random import shuffle
from random import  randint


# initial list
sticks = ['-', '--', '---', '----']

# mixing sticks
def mix(my_list):
    shuffle(my_list)
    return my_list

# choose number
def try_your_luck():
    a_try=''
    while a_try not in ['1', '2', '3', '4']:
        a_try = input("choose a number: ")

    return int(a_try)

# check players try
def verify_try(a_list, a_try):
    if a_list[a_try - 1] == '-':
        print("Wash the dishes")
    else:
        print("This time you are safe")

    print(f"You got {a_list[a_try-1]}")

mixed_sticks = mix(sticks)
selection = try_your_luck()
verify_try(mixed_sticks, selection)

"The sum of your dice is {suma_dados}. Unfortunate"
"The sum of your dice is {suma_dados}. You have a good chance"
"The sum of your dice is {sum_dice}. It looks like a winning roll"

def throw_dice():
    first = randint(1, 6)
    second=randint(1, 6)
    return first, second

def roll_result(first, second):
    sum_dice = first + second
    if sum_dice <= 6:
        return f"The sum of your dice is {sum_dice}. Unfortunate"
    elif sum_dice >= 10:
        return f"The sum of your dice is {sum_dice}. It looks like a winning roll"
    else:
        return f"The sum of your dice is {sum_dice}. You have a good chance"

def number_attributes(**kwargs):
    no_items = 0
    for item in kwargs.keys():
        no_items += 1

def list_attributes(**kwargs):
    list = []
    for item in kwargs.values():
        print(item)
        list.append(item)
