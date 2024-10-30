# Import way 1: from functions import get_todos, write_todos
import functions
get_todos = functions.get_todos
write_todos = functions.write_todos
import time

while True:
    user_action = input("Enter add, edit, complete or show :")
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:] #cắt chuỗi từ vị trí thứ 4 đến hết

        todos = get_todos()

        todos.append(todo.capitalize() + '\n')

        write_todos(todos)
    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            print(f'{index + 1}. {item.strip()}') #strip để xóa ký tự xuống dòng
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()

            if 0 <= number < len(todos):
                print(f'Item u want to change at position {number} is: {todos[number]}')
                new_todo = input('Enter new todo: ')
                todos[number] = new_todo.capitalize() + '\n'
                write_todos(todos)

            else:
                print('number must greater than 0 and less than ', len(todos))
        except ValueError:
            print('Invalid number')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()

            todos.pop(number - 1)
            write_todos(todos)

        except IndexError:
            print('There is no item at position ', number)
            continue

    elif user_action.startswith('end'):
        break
    else :
        print('Invalid action')
        continue
print('Goodbye')