user_prompt = "Enter a todo: "
todos = []
while True:
    todo = input(user_prompt)
    todo.capitalize()
    todos.append(todo)
    print(todos)