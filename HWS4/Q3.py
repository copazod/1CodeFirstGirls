# Write a program that simulates a lottery.
# The program should have a list of seven numbers that represent a lottery ticket.
# It should then generate seven random numbers.
# After comparing the two sets of numbers, the program should output a prize based
# on the number of matches:
# ● £20 for three matching numbers
# ● £40 for four matching numbers
# ● £100 for five matching numbers
# ● £10000 for six matching numbers
# ● £1000000 for seven matching numbers

import random

lottery_ticket = [54,89,32,14,21,12,44]
number_drop = list()
match_point=0
print(lottery_ticket)

for i in range(7):
    random_num = random.randint(1,100)
    number_drop.append(random_num)
print(number_drop)

for n in lottery_ticket:
    if n in number_drop:
        match_point=match_point+1
print(match_point)

if match_point==1:
    print("Price: £20")
elif match_point==2:
    print("Price: £40")
elif match_point==5:
    print("Price: £100")
elif match_point==6:
    print("Price: £10000")
elif match_point==7:
    print("Price: £1000000")
else:
    print("Good luck next time!")





