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
    user_action = input("Enter add, edit or show :")
    user_action = user_action.strip().lower()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            file = open('./basics/todos.txt', 'r')
            todos = file.readlines()
            file.close() #đóng file để tránh lỗi

            todos.append(todo.capitalize())
            
            file = open('./basics/todos.txt', 'w') #a là append, w là write, r là read
            file.writelines(todos)
            file.close()
        case 'show' | 'list':
            file = open('./basics/todos.txt', 'r')
            todos = file.readlines()
            file.close() #có thể đóng file luôn vì giá trị được lưu trong biến todos rồi

            for index, item in enumerate(todos):
                print(f'{index + 1}. {item.strip()}') #strip để xóa ký tự xuống dòng
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
        case 'complete':
            number = int(input('Number of the todo to complete:'))
            todos.pop(number - 1)
        case 'end':
            break
        case default:
            print('Invalid action')
            continue
print('Goodbye')