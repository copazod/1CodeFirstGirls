# dictionary_name = {key:value}

menu = {"pizza":5, "burger":3, "noodles":2}
print(menu["pizza"])
print(" ")

for item in menu:
    print(item)
print(" ")
for item in menu.values():
    print(item)
print(" ")
for item in menu.items():
    print(item)
print(" ")
for item,price in menu.items():
    print(item, price)
print(" ")

# Dictionary inside another dictionary
person = {"name":"Tom", "age":23, "address":{'city':'London', 'street':123}}

print(person["name"])
print(person["age"])
print(person["address"]["city"])
print(" ")

# lists in dictionaries
people = [{'name':'Tom', 'age':23},{'name':'Nick', 'age':30}]
for person in people:
    print(person["name"])


