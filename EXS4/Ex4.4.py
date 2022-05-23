# Write a program that uses a for loop to calculate the total cost

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0


for item in costs:
    total_cost = total_cost + item

print("Total cost of the week: ", total_cost)
print("Spend average per week: ", total_cost/(len(costs)))

