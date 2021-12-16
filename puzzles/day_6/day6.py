def get_unique_answers(response):
    questions = []

    for char in response:
        if char not in questions:
            questions.append(char)

    return len(questions)


with open ('inputday6.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]

sum = 0
currentResponse = ''
for line in data:
    if line != '':
        currentResponse += line
    else:
        sum += get_unique_answers(currentResponse)
        currentResponse = ''

sum += get_unique_answers(currentResponse)

print(sum)

# part 2

sum = 0
