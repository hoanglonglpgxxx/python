filenames = ['1.data1.csv', '2.data2.csv', '3.data3.csv']

for filename in filenames:
    filename = filename.replace('.', '-', 1);# 1 là số lần thay thế
    print(filename)