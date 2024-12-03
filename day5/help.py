dic = {'key1':100, 'key2':200}
dic.values()

text = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

text = text.lstrip(",").lstrip(":").lstrip('%').lstrip('_').lstrip('#')
print(text)

text = text.lstrip(",:_#%")

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3, "orange")
print(fruits)

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolated_sets = phone_brands.isdisjoint(tv_brands)
print(isolated_sets)

def welcome(name: str):
    print(f"Welcome {name}")


def revers_word(word):
    return "".join(reversed(word))

word = "python"

revers_word(word).upper()