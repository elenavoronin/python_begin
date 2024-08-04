def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_local):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)


while True:
    user_action = input("Type add, show, edit ,complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos("todos.txt")
        todos.append(todo.title() + "\n")
        write_todos("todos.txt", todos)
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            todos = get_todos("todos.txt")
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) - 1
            todos = get_todos("todos.txt")
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
            write_todos("todos.txt", todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except (IndexError, ValueError):
            print("Your command is not valid.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye!")
