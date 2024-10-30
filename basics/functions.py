def get_todos(filepath="./basics/todos.txt"): #đọc file và trả về list
    """ Read todos from file and return as a list """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local
 
def write_todos(todos_local, filepath="./basics/todos.txt"): #ghi vào file
    """ Write todos to file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)

if __name__ == "__main__": #chỉ chạy khi file này được chạy trực tiếp, không chạy khi được import
    print("This is functions.py")
    write_todos(get_todos())