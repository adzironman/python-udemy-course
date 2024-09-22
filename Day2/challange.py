name = input("What's your name? ")
sales = input("What's your sales? ")

commission = round(0.13 * float(sales), 2)
print(f"Hello {name}, your commission is {commission}")