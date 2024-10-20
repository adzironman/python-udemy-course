my_tuple = (1, 2, 3, (43,'dasd'))
print(type(my_tuple))

x, y, z, a = my_tuple
print(x, y, z, a)

t = (5, 5.6, 'hello', [1, 2, 3])
my_list = list(t)
print(type(my_list))


print(t.index('hello'))
print(t.count(5))