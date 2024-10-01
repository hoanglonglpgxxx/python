""" user_prompt = "Enter a todo \'t:"

todo1 = input(user_prompt)#truyền vào string khởi đầu trước khi nhập
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3, "Hello", "a"]

print(todos)
print(type(todos)) """

""" title = input('Enter title: \t')
print(title)
print('length of title: ', len(title)) """

todos = []

while True:
    user_action = input("Enter add, edit or show :")
    user_action = user_action.strip().lower()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show' | 'list':
            for item in todos:
                print(item)
        case 'edit': 
            number = int(input('Enter position of action u want to change: '))
            number = number - 1
            if 0 <= number < len(todos):
                print(f'Item u want to change at position {number} is: {todos[number]}')
                new_todo = input('Enter new todo: ')
                todos[number] = new_todo.capitalize()
                print('Updated list: ', todos)
            else:
                print('number must greater than 0 and less than ', len(todos))
        case 'end':
            break
        case default:
            print('Invalid action')
            continue
print('Goodbye')