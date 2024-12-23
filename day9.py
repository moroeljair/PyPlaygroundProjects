while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo+'\n')

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif ('show' in user_action) | ('display' in user_action):
        file = open('files/todos.txt', 'r')
        todos = file.readlines()
        file.close()

        # new_todos = [item.strip('\n') for item in todos]

        for index,item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item.title()}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number-1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input('Enter a new todo: ')
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[number - 1].strip('\n')
        todos.pop(number - 1)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from de list. "
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print('Command is not valid.')

print("Bye!")