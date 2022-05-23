#Exercise 3.1: You have a budget of £10 and want to write a
# program to decide which burger restaurant to go to.
#1. Input the price of a burger using input()
#2. Check whether the price is less than or equal (<=) 10.00
#3. Print the result in the format below
#int: remember to convert the input from a string to a decimal with float()

BP = input('Put price of the burger: ')

Budget = float(BP)<= 10
#print('We are going {}'.format(Budget))

# Add code to your burger program to input whether the restaurant
# has a vegetarian option. The output should say whether the
# cost is within budget AND has a vegetarian option

rest = input('Is it have a vegetarian option? ')

x = rest == 'y'
should_go = Budget and x

print('Can we go? {}'.format(should_go))

if should_go:
    print('Restaurant is a good choice')
else:
    print('another time')