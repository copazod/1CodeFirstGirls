#In a new Python file called cat_food.py, create a program that calculates how many
# cans of cat food you need to feed 10 cats. Your will need:
#1. A variable for the number of cats
#2. A variable for the number of cans each cat eats in a day
#3. A print() function to output the result
#Extension: change the calculation to work out the amount needed for 7 days

nofcat = int(input("How many cats do you have?"))
canpcat = int(input("How many cans your cat eats per day?"))
tcan = nofcat*canpcat

canwk = tcan*7

print(f"To feed your {nofcat} cats, you need {tcan} can per day and {canwk} per week.")
print("To feed your {} cats, you need {} can per day and {} per week.".format(nofcat,tcan,canwk))