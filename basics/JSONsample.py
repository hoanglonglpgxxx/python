import json

with open('basics/questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alnernative in enumerate(question["alternatives"]):
        print(f"{index+1}-{alnernative}")
    user_choice = int(input('Enter ur answer: '))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score+=1

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score+=1
        result = 'Correct answer'
    else:
        result = 'Wrong answer'

    msg = f"{index+1} - {result} - Your answer: {question['user_choice']}"\
      f"{',Correct answer: ' + str(question['correct_answer']) if result == 'Wrong answer' else ''}"
    print(msg)
print(f'ur score: {score}/{len(data)}')