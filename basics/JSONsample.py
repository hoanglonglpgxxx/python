import json

with open('basics/questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

print(data, type(data))