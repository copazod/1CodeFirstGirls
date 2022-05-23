#Whenever I'm shopping and I buy some bread I always forget to buy
# butter. Create a list and if 'bread' is in the list, add 'butter'
# to the shopping list. Try running the program with and without bread
# in the list to check that your program works. Remember the in operator
# checks if an item is in a list and the .append() method adds an item to
# a list

food = ["bread", "eggs", "jam"]

if "bread" in food:
    food.append("butter")
    print(food)
else:
    print("bread not found")

count = 0
for i in food:
    print(i)
    count = count + 1
print("number of items: ", count)