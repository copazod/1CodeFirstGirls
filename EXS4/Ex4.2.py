scores = [159, 85, 66, 72, 54, 43, 23, 14,92, 34]

print(len(scores))
print(max(scores))
print(min(scores))

# 2 maneras de hacer sort:

scores.sort()
print(scores)

print(sorted(scores))

# orden de mayor a menor
scores.sort(reverse=True)
print(scores)