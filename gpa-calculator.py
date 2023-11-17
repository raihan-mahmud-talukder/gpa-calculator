# GPA Calculator

bangla = int(input('Bangla: '))
english = int(input('English: '))
math = int(input('Math: '))
science = int(input('Science: '))

result = (bangla + english + math + science) / 4

grade = ''

if bangla < 0 or english < 0 or math < 0 or science < 0 or bangla > 100 or english > 100 or math > 100 or science > 100:
    print('Input out of range')
else:
    if result >= 0 and result <= 40:
        grade = 'F'
    elif result > 40 and result <= 60:
        grade = 'D'
    elif result > 60 and result <= 70:
        grade = 'C'
    elif result > 70 and result <= 80:
        grade = 'B'
    elif result > 80 and result <= 90:
        grade = 'A'
    elif result > 90 and result <= 100:
        grade = 'A+'
    else:
        grade = 'Invalid Input'
    print(f'Result: {result}, Grade: {grade}')