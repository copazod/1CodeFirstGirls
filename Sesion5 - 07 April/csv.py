

# creat spread sheet using python
import csv

header = ["name","age"]

data = [
    {"name": "Bill", "age": "33"},
    {"name": "Tom", "age": "31"}
]

with open("aFileRandomName.csv", "w") as aFile:
    spreed = csv.DicWriter(aFile, fieldnames=header)
    spreed.writeheader()
    spreed.writerows(data)
