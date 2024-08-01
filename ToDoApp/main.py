user_prompt = "Type add, show, edit ,complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if "add" in user_action or "new" in user_action:
        todo = user_action[4:]
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif "show" in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif "edit" in user_action:
        number = int(user_action[5:]) - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif "complete" in user_action:
        number = int(user_action[9:]) - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todo_to_remove = todos[number].strip('\n')
        todos.pop(number)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)
    elif "exit" in user_action:
        break
    else:
        print("Command is not valid")
print("Bye!")
