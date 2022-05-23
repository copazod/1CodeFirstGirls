colors=["red", "green", "blue", "black"]
colors.append("white")
print(colors)
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(' ')


for i in colors:
    print(i)
print(' ')

colors=["red", "green", "blue", "black"]
colors.append('white')
colors.insert(2,'pink')
print(colors)
print(' ')

colors=["red", "green", "blue", "black"]
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
colors.pop(0)
colors.remove("green")
print(colors)
print(' ')


colors=["red", "green", "blue", "black"]
colors_2021 = colors.copy()
colors_2021.remove("red")
print('colors2021:',colors_2021)
print(' ')

#add values of 1 list to another list
colors=["red", "green", "blue", "black"]
colors_2021 = ["gold", "silver"]
colors.extend(colors_2021)
print(colors_2021)
print(colors)
print(' ')

#change value of a list
colors=["red", "green", "blue", "black"]
colors[0] = "gold"
print(colors)
print(' ')

#to check what is on the list

students = ["Tom", "Nick", "Sam", "Millie"]
stud = input("Enter the name of student: ")

if stud in students:
    print(f'{stud} is there')
else:
    print(f"{stud} is not there.")

students = ["Tom", "Nick", "Sam", "Millie"]
print(len(students))
marks = [40,50,80,60]
max = max(marks)
min = min(marks)
