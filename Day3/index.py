my_text = "This text is a test"
# result = my_text.index("text")
# result = my_text.index("s") #find first
# result = my_text.index("s", 5) #find first after index 5
# result = my_text.index("s", 5, 11) #find first after index 5 to 11

result = my_text.rindex("s") #search from right

print(result)