#Exercise 4.3
#Whenever I'm shopping and I buy some bread I always forget to buy butter.
# Create a list and if 'bread'is in the list, add 'butter' to the shopping list.
#Try running the program with and without bread in the list to check that your program works.
#Remember the in operator checks if an item is in a list and
# the .append() method adds an item to a list.
#Extension:only add butter to the list if it is not already in the list

shopl=["butter","bread","eggs", "milk"]

if "bread" in shopl:
    if "butter" in shopl:
        print("Butter is already in the list.", shopl)
    else:
        shopl.append("butter")
        print(shopl)
else:
    print("There is no bread.")


