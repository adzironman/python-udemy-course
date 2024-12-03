

def check_3_digits(number):
    return number in range(100, 1000)

result = check_3_digits(423)
print(result)

def all_positives(list):
    for item in list:
        if item >= 0:
            continue
        else:
            return False

    return True

list_of = [1, 3, 342, 42, -3123, 312]
print(all_positives(list_of))

def sum_less(numbers):
    sum = 0
    for item in numbers:
        if  1000 > item > 0:
            sum = sum+item

    return sum

numbers = [123, 123, 34, 123, -12, -23, 213123]

print(sum_less(numbers))

def count_even(numbers):
    counter = 0
    for item in numbers:
        if item%2==0:
            counter = counter +1

    return counter

numbers = [2, 34, 213, 3213, 43, 2, -123]

print(count_even(numbers))

