my_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(my_set))
print(my_set)

other_set = {1, 2, 3}
print(type(other_set))
print(other_set)

print(3 in my_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)