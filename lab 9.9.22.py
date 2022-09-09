lab_weight = 0.7
exam_weight = 0.2
attendance_weight = 0.1

print('**** Welcome to the LAB grade calculator! ****')
user_name = input('Who are we calculating grades for? ==>')
lab_grade = int(input('Enter the Labs grade? ==>'))
if lab_grade >= 100: #if user inputs value greater than 100 program will change it to 100
        print('The lab value should have been 100 or less. It has been changed to 100.')
        lab_grade == 100 #expression that will change grade if exceeds 100
elif lab_grade <= 0:
        print('The lab value should have been zero or greater. It has been changed to zero')
        lab_grade == 0 #expression that will change grade if below 0
exam_grade = int(input('Enter the EXAMS grade? ==>'))
if exam_grade >= 100:
        print('The exam value should have been 100 or less. It has been changed to 100.')
        exam_grade == 100
elif exam_grade <= 0:
        print('The exam value should have been zero or greater. It has been changed to zero')
        exam_grade == 0
attendance_grade = int(input('Enter the attendance grade? ==>'))
if attendance_grade >= 100:
        print('The attendance value should have been 100 or less. It has been changed to 100.')
        attendance_grade == 100
elif attendance_grade <= 0:
        print('The attendance value should have been zero or greater. It has been changed to zero')
        attendance_grade == 0
weight_grade = float((lab_grade * lab_weight) + (exam_grade * exam_weight) + (attendance_weight * attendance_weight))#float in beggining to change input from integers
print(f'The weighted grade for {user_name} is {weight_grade}')
if weight_grade > 90 and weight_grade <= 100: #user falls in range between one of the letter grades
    print(f'{user_name} has a letter grade of A')
elif weight_grade <= 89 and weight_grade >= 80:
    print(f'{user_name} has a letter grade of B')
elif weight_grade <= 79 and weight_grade >= 70:
    print(f'{user_name} has a letter grade of C')
elif weight_grade <= 69 and weight_grade >= 60:
    print(f'{user_name} has a letter grade of D')
else:
    print(f'{user_name} has a letter grade of F')
print('**** Thanks for using the Lab grade calculator ****')

