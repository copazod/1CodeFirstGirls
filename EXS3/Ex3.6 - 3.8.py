import random

def flip_coin():
    random_number = random.randint(1, 2)
    if random_number == 1:
        side = 'heads'
    else:
        side = 'tails'
    return side

while True:
    choice = input('heads or tails: ')

    if choice != 'heads' and choice != 'tails':
        print("Incorrect input.")
        continue

    if choice == 'heads'or choice == 'tails':
        break

result = flip_coin()
print('The coin landed on {}'.format(result))

if result == choice:
    print("You won!")
else:
    print("You lost!")