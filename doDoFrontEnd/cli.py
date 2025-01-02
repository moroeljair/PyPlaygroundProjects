from functions import get_todos, write_todos
# import functions #si usas asi tienes que llamar functions.nombre_de_la_funcion

import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo+'\n')

        write_todos(filepath='files/todos.txt', todos_arg=todos)

    elif (user_action.startswith("show")) | (user_action.startswith("display")):
        file = open('files/todos.txt', 'r')
        todos = file.readlines()
        file.close()

        # new_todos = [item.strip('\n') for item in todos]

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item.title()}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = get_todos()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError: #Existen diferentes tipos de errores: ValueError, IndexError, SyntaxError, TypeError, ...
            print("Your command is not valid.")
            continue #salta al inicio del while

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            write_todos(todos, 'files/todos.txt')

            message = f"Todo {todo_to_remove} was removed from de list. "
            print(message)
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print('Command is not valid.')

print("Bye!")

