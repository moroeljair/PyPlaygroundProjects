while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip('\n') for item in todos]

            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item.title()}"
                print(row)
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number-1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input('Enter a new todo: ')
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input('Number of the todo to complete: '))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from de list. "
            print(message)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")