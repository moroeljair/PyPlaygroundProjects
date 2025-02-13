FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in a text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__) #es el valor del nombre del archivo, cuando se ejecuta el mismo es '__main__', de otro lado es el nombre

def foo(n1, n2=2, n3=3):
    r = n1*n2*n3
    return r

#solo ejecutar cuando se ejecute este archivo y no cuando se importe de otro lado
if __name__ == '__main__':
    print("hello from functions")
    print(get_todos())
    print(foo(20,2))
