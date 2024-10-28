""" user_prompt = "Enter a todo:"

todo1 = input(user_prompt)#truyền vào string khởi đầu trước khi nhập
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3, "Hello", "a"]

print(todos)
print(type(todos)) """

""" title = input('Enter title: \t')
print(title)
print('length of title: ', len(title)) """


""" filenames = ['1.data1.csv', '2.data2.csv', '3.data3.csv']

for filename in filenames:
    filename = filename.replace('.', '-', 1);# 1 là số lần thay thế
    print(filename) """

def get_todos(filepath): #đọc file và trả về list
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_local): #ghi vào file
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)

while True:
    user_action = input("Enter add, edit, complete or show :")
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:] #cắt chuỗi từ vị trí thứ 4 đến hết

        todos = get_todos('./basics/todos.txt')

        todos.append(todo.capitalize() + '\n')

        write_todos('./basics/todos.txt', todos)
    elif user_action.startswith('show'):
        todos = get_todos('./basics/todos.txt')

        for index, item in enumerate(todos):
            print(f'{index + 1}. {item.strip()}') #strip để xóa ký tự xuống dòng
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos('./basics/todos.txt')

            if 0 <= number < len(todos):
                print(f'Item u want to change at position {number} is: {todos[number]}')
                new_todo = input('Enter new todo: ')
                todos[number] = new_todo.capitalize() + '\n'
                write_todos('./basics/todos.txt', todos)

            else:
                print('number must greater than 0 and less than ', len(todos))
        except ValueError:
            print('Invalid number')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos('./basics/todos.txt')

            todos.pop(number - 1)
            write_todos('./basics/todos.txt', todos)

        except IndexError:
            print('There is no item at position ', number)
            continue

    elif user_action.startswith('end'):
        break
    else :
        print('Invalid action')
        continue
print('Goodbye')