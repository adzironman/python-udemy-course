analyzing_test = input('''Hey there!
Send me a text to analyze: ''')

letters = input("Thank you! Now, send me 3 a letters to analyze: ")
letters = letters.replace(" ", "")
first_letter_count = analyzing_test.lower().count(letters[0].lower())
second_letter_count = analyzing_test.lower().count(letters[1].lower())
third_letter_count = analyzing_test.lower().count(letters[2].lower())

print(f"\n1. Your text has {first_letter_count} letters {letters[0]}")
print(f"\n2. Your text has {second_letter_count} letters {letters[1]}")
print(f"\n3. Your text has {third_letter_count} letters {letters[2]}")
print(f"\n4. Your text has {len(analyzing_test)} characters ")

print(f"\n5. Your text has {len(analyzing_test.split())} words")
first_letter = analyzing_test[0]
last_letter = analyzing_test[-1]
print(f"\n6. First letter is: {first_letter}")
print(f"\n7. Last letter is: {last_letter}")

list_of_words = analyzing_test.split()
print(list_of_words)
print(type(list_of_words))
reverse = list_of_words.reverse()
print(f"\n8. Reverse words order {list_of_words}")
