#spreadsheet = # Add code to open the csv file
import csv

with open("trees.csv","r") as afile:
    spreadsheet = csv.DictReader(aFile)

    heights = []
    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)
