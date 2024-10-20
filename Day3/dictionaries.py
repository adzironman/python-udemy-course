my_dictionary = { "c1":"value", "c2":"value2", "c3":"value3" }
print(type(my_dictionary))

print(my_dictionary)

result = my_dictionary["c2"]
print(result)

customer = {'name': 'John', 'last_name':'Wald', 'weight': 88, 'height': 123}
print(customer['last_name'])

dic = {1: 55, 2:[1,2,3], 3: {'s1':100, 's2':200}, 'test': 'test'}
print(dic[3]['s2'])
print(dic[2][1])
print(dic['test'])

dic2 = {'k1':['a', 'b', 'c'], 'k2': ['d', 'e', 'f']}
print(dic2['k2'][1].upper())

dic3 = {1: 100, 2: 200}
dic3[3] = 300

print(dic3)

dic3.pop(2)
print(dic3)
dic3.update()