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

while True:
    user_action = input("Enter add, edit, complete or show :")
    user_action = user_action.strip().lower()

    if 'add' in user_action:
        todo = user_action[4:] #cắt chuỗi từ vị trí thứ 4 đến hết

        with open('./basics/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo.capitalize() + '\n')

        with open('./basics/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open('./basics/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            print(f'{index + 1}. {item.strip()}') #strip để xóa ký tự xuống dòng
    elif 'edit' in user_action: 
        number = int(user_action[5:])
        number = number - 1
        with open('./basics/todos.txt', 'r') as file:
            todos = file.readlines()

        if 0 <= number < len(todos):
            print(f'Item u want to change at position {number} is: {todos[number]}')
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo.capitalize() + '\n'
            with open('./basics/todos.txt', 'w') as file:
                file.writelines(todos)
        else:
            print('number must greater than 0 and less than ', len(todos))
    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('./basics/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(number - 1)
        with open('./basics/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'end' in user_action:
        break
    else :
        print('Invalid action')
        continue
print('Goodbye')