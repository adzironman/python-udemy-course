text = "We are going to learn six string methods today"

result = text.upper()
print(result)

result = text[4].upper()
print(result)

result = text.split()
print(result)

result = text.split(" ", 3)
print(result)

a = "learning"
b = "Python"
c = "is"
d = "fun"

result = " ".join([a, b, c, d])
print(result)

result = text.replace("six", "4")
print(result.replace(" ", ""))
