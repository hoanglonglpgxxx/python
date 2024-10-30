import glob

myfiles = glob.glob('basics/files/*.txt')

for filepath in myfiles:
    """Get content in all files in folder "files" """
    with open(filepath, 'r') as file:
        print(file.read().upper())