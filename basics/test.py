# 1. Create a list of 3 items and a list of 3 filenames. Loop through the list of filenames and write each item from the list of items to the corresponding filename.
""" contents = ["text1", "text2", "text3"]

filenames = ['data1.csv', 'data2.csv', 'data3.csv'] """

# C1
""" for index, filename in enumerate(filenames):
    for index2, content in enumerate(contents):
        with open(f'./basics/{filename}', 'a') as file:
            if index2 == index:
                file.write(f'{contents[index2]}\n')  """

# C2
""" for content, filename in zip(contents, filenames): #zip để ghép 2 list lại với nhau, nếu 1 list dài hơn thì sẽ bỏ qua
    with open(f'./basics/{filename}', 'w') as file:
        file.write(content)
 """

# date = input('Enter date: ')
# mood = input('Enter mood: ')
# journal = input('Enter journal: \n')

# with open(f"../journal/{date}.txt", 'w') as file:
#     file.write(f'{mood}\n')
#     file.write(f'{journal}\n')
#     file.write('\n')


#C3. check password
password = input('Enter password: ')

result = {}

if len(password) >= 8:
    result['length'] = (True)
else :
    result['length'] = (False)

digit = False
uppercase = False
for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        uppercase = True
result['digit'] = digit
result['uppercase'] = uppercase
print('Password is valid' if all(result) else 'Password is invalid')
