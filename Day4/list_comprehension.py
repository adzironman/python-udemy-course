from heapq import merge

word = 'python'
list = []

for letter in word:
    list.append(letter)

print(list)

comprehension_list = [ll for ll in word]

print(comprehension_list)

another_list = [n for n in range(0, 21, 2)]
print(another_list)

another_list = [n / 2 for n in range(0, 21, 2)]
print(another_list)

another_list = [n for n in range(0, 21, 2) if n * 2 > 10]
print(another_list)

another_list = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
print(another_list)

feet = [10, 20, 30, 40, 50]

meters = [n*0.3048 for n in feet]
print(meters)
