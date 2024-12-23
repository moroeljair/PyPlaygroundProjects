user_prompt = "Enter a todo:"
todo1=input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3,'Hello Jair']
print(todos)

print(type(user_prompt))
print(type(todos))

for item in ["hello", "hi"]:
    print(item.upper())

for i, j in enumerate("abcd"):
    print(j.capitalize())
