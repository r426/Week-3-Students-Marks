#input: five marks (1 - 100)
#output: average and grade (A - F)

numberOfMarks = 5
marks = []
sum = 0

for i in range(numberOfMarks):
    enteredMark = -1
    while enteredMark < 0 or enteredMark > 100:
        userInput = input('\nEnter the mark:')
        if userInput.isnumeric():
            enteredMark = int(userInput)
            if enteredMark > 100:
                print("Input error.")
        else: print("Input error.")
    marks.append(enteredMark)
    sum += marks[i]
    for j in range(len(marks)):
        print('Mark No.{} is {}'.format(j + 1, marks[j]))

average = sum / numberOfMarks
if average >= 90: grade = 'A'
elif average >= 80: grade = 'B'
elif average >= 70: grade = 'C'
elif average >= 60: grade = 'D'
else: grade = 'F'

print('\nYour marks:', end=' ')
for x in marks:
    print(x, end=' ')
print('\nYour average:', average)
print('Your grade:', grade)
