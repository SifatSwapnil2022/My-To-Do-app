FILEPATH ="todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    To-Do items.
    """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the To-Do items list in the text files."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())