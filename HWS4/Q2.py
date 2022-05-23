# I'm setting up my own market stall to sell chocolates.
# I need a basic till to check the prices of different chocolates that I sell.
# I've started the program and included the chocolates and their prices.
# Finish the program by asking the user to input an item and then output its price.

chocolates = { 'white': 1.50, 'milk': 1.20, 'dark': 1.80, 'vegan': 2.00 }

prc = input("Introduce type of chocolate: ")

if prc == 'white':
    print('Price: ', chocolates['white'])
elif prc == 'milk':
    print('Price: ', chocolates['milk'])
elif prc == 'dark':
    print('Price: ', chocolates['dark'])
elif prc == 'vegan':
    print('Price: ', chocolates['vegan'])
