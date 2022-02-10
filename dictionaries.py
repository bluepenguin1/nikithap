lloyd = {'name': 'Lloyd', 'homework':[90.0, 97.0, 75.0, 92.0], 'quizzes':[88.0, 40.0, 94.0], 'tests':[75.0, 90.0]}
alice = {'name': 'Alice','homework':[91.4, 99.9, 11.4], 'quizzes':[89.3, 87.8, 56.0], 'tests':[73.9, 21.4]}
tyler = {'name': 'Tyler','homework':[78.5, 34.9, 22,9], 'quizzes':[99.8, 67.8, 100.0], 'tests':[100.0, 100.0]}

students = [lloyd, alice, tyler]

for x in students:
    print(x)
    
def average(num):
    total = float(sum(num))
    avg = total / len(num)
    return avg

print('Student average is ' + str(average(lloyd['homework'])))

def get_average(student):
    homework = student['homework']
    quizzes = student['quizzes']
    tests = student['tests']
    avg = average(homework)* 0.1 + average(quizzes)* 0.3 + average(tests)* 0.6
    return avg

print('Lloyd average is ' + str(get_average(lloyd)))

def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print('Lloyd letter grade is ' + str(get_letter_grade(get_average(lloyd))))

def get_class_average(students):
    results = []
    for tea in students:
        results.append(get_average(tea))
    return results

print('Class average is ' + str(get_class_average(students)))
      
