#Exercise 4.2: Make a list of game scores.
# Using list functions write code to output information
# of the scores in the following format:
# Extension: Output all of the scores in descending order
# Number of scores: 10 Highest score: 200 Lowest score: 3

scores = [200,150,300,230]
max = max(scores)
min = min(scores)

scores.sort(reverse=True)
print(scores)
