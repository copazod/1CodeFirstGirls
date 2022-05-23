
# Using a for loop,out put the values name, colour and price of each dictionary in the list
# Extension: Add more items to the list

fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19}]

# option 1: using index
print(fruits[0]['name'])
print(fruits[0]['colour'])
print(fruits[0]['price'])
print(fruits[1]['name'])
print(fruits[2]['name']) #etc...
print()

# option 2: using loop
# iterate over the list
for i in fruits:
# now iterate over the values of the dict
    for value in i.values():
    # print every key of each dict
        print(value)

# Add a dictionary to the list

fruits.append({'name': 'kiwi', 'colour': 'green', 'price': 0.22})
print(fruits)
print()

for key, val in fruits[0].items():
    print("{} : {}".format(key, val))




