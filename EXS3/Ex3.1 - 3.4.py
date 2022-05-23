bp= float(input("What's the burger's price?"))

budget = bp <= 10
print("Burger is within budget: {}".format(budget))

vg=input("Has the restaurant a vegetarian option: ")

cond = vg == 'y'
wego = cond and budget

print("Restaurant meets criteria: {}".format(wego))

rate=int(input("How many stars has the restaurant?"))

st = rate >= 3
print("The restaurant rating over 3 stars: {}".format(st))

if rate >= 3:
    print("This restaurant is a good choice!")
else:
    print("Probably not a good idea")