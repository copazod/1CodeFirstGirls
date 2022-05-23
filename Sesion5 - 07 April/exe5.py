


new_item = input("enter to do list")

with open('todo.txt','r') as todo_file:
    todo = todo_file.read()

todod = todo + new_item + '\n'

with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)
    