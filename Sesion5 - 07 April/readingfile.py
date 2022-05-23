# 1.  ask user to input a new to do item, store it in a var

# 2.  use "with open" to open/create a new file called "todo.txt"
# 2.1 read the contents of todo.txt and store it in a new var called todo

# 3.  add the user input to the todo var and save it as itself


# 4.  use "with open" to open the todo.txt file as writable
# 4.1 write the content of the todo var into the file using "write()" method


#with open("people.txt","r") as afile:
#    ppl = afile.read()

data = "Lilly, Bess, Anuj"

with open("friends.txt","w") as afile:
    afile.write(data)


