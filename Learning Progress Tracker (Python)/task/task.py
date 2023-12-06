import re
from functools import cmp_to_key

help_functions = ['add students', 'list', 'add points', 'find', 'statistics', 'notify', 'exit']


class StringId(Exception):

    def __str__(self):
        return 'ID\'s can only be numbers!'


class Student:
    student_num = 5356

    def __init__(self, first_name, last_name, email, python=0, dsa=0, databases=0, flask=0):
        self.id = Student.student_num + 1
        self.python = python
        self.dsa = dsa
        self.databases = databases
        self.flask = flask
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.notified_python = False
        self.notified_dsa = False
        self.notified_databases = False
        self.notified_flask = False
        Student.student_num += 1


def check_email(email):
    pattern = r"[a-zA-Z0-9.]+@[a-zA-Z0-9]+[.][a-zA-Z0-9]+"
    return bool(re.match(pattern, email))


# checks for double hyphens or apostrophes
def check_doubles(name):
    pattern = r"['-]['-]"
    return bool(re.search(pattern, name))


def check_name(name):
    pattern = r"[^-'][\.^a-zA-Z^\-\']*[a-zA-Z\-{1}\'{1}]*[^\-\']"
    lst = name.split()
    for n in lst:
        if re.search(pattern, n) is None:
            return False
        if not (re.search(pattern, n).group(0) == n and not check_doubles(n)):
            return False
    return True


# 1 - python
# 2 - dsa
# 3 - databases
# 4 - flask
def calculate_total_enrollment(student_l, course):
    total = 0
    for student in student_l:
        match course:
            case 1:
                if student.python != 0:
                    total += 1
            case 2:
                if student.dsa != 0:
                    total += 1
            case 3:
                if student.databases != 0:
                    total += 1
            case 4:
                if student.flask != 0:
                    total += 1
    return total


def calculate_most_popular(student_l):
    total_python = calculate_total_enrollment(student_l, 1)
    total_dsa = calculate_total_enrollment(student_l, 2)
    total_databases = calculate_total_enrollment(student_l, 3)
    total_flask = calculate_total_enrollment(student_l, 4)
    most_enrolled = max(total_python, total_dsa, total_databases, total_flask)

    most_popular = []

    if total_python == most_enrolled and total_python != 0:
        most_popular.append('Python')
    if total_dsa == most_enrolled and total_dsa != 0:
        most_popular.append('DSA')
    if total_databases == most_enrolled and total_databases != 0:
        most_popular.append('Databases')
    if total_flask == most_enrolled and total_flask != 0:
        most_popular.append('Flask')

    if len(most_popular) == 0:
        return None
    else:
        return most_popular


def calculate_least_popular(student_l):
    total_python = calculate_total_enrollment(student_l, 1)
    total_dsa = calculate_total_enrollment(student_l, 2)
    total_databases = calculate_total_enrollment(student_l, 3)
    total_flask = calculate_total_enrollment(student_l, 4)
    least_enrolled = min(total_python, total_dsa, total_databases, total_flask)

    least_popular = []

    if total_python == least_enrolled:
        least_popular.append('Python')
    if total_dsa == least_enrolled:
        least_popular.append('DSA')
    if total_databases == least_enrolled:
        least_popular.append('Databases')
    if total_flask == least_enrolled:
        least_popular.append('Flask')

    if len(least_popular) == 4:
        return None
    else:
        return least_popular


def calculate_highest_activity(python, dsa, databases, flask):
    maximum = max(python, dsa, databases, flask)
    lst = []

    if maximum == python:
        lst.append('Python')
    if maximum == dsa:
        lst.append('DSA')
    if maximum == databases:
        lst.append('Databases')
    if maximum == flask:
        lst.append('Flask')

    return lst


def calculate_lowest_activity(python, dsa, databases, flask):
    lst = []

    if 0 != python:
        lst.append(python)
    if 0 != dsa:
        lst.append(dsa)
    if 0 != databases:
        lst.append(databases)
    if 0 != flask:
        lst.append(flask)
    if len(lst) != 1:
        return None
    minimum = min(lst)
    if python == minimum:
        return 'Python'
    if dsa == minimum:
        return 'DSA'
    if databases == minimum:
        return 'Databases'
    if flask == minimum:
        return 'Flask'

    return None


def calculate_average_activity(student_l, course):
    total = 0
    enrolled_num = 0
    for student in student_l:
        match course:
            case 1:
                if student.python:
                    total += student.python
                    enrolled_num += 1
            case 2:
                if student.dsa:
                    total += student.dsa
                    enrolled_num += 1

            case 3:
                if student.databases:
                    total += student.databases
                    enrolled_num += 1
            case 4:
                if student.flask:
                    total += student.flask
                    enrolled_num += 1
    try:
        return total / enrolled_num
    except ZeroDivisionError:
        return None


def get_highest_integer(lst):
    highest_integer = None
    for num in lst:
        if num is not None and (highest_integer is None or num > highest_integer):
            highest_integer = num
    return highest_integer


def get_lowest_integer(lst):
    lowest = None
    for num in lst:
        if num is not None and (lowest is None or num < lowest):
            lowest = num
    return lowest


def calculate_easiest_course(student_l):
    average = []
    for i in range(1, 5):
        average.append(calculate_average_activity(student_l, i))
    maximum = get_highest_integer(average)
    if maximum is None:
        return None
    for i in range(len(average)):
        if maximum == calculate_average_activity(student_l, i):
            match i:
                case 1:
                    return 'Python'
                case 2:
                    return 'DSA'
                case 3:
                    return 'Databases'
                case 4:
                    return 'Flask'


def calculate_hardest_course(student_l):
    average = []
    for i in range(1, 5):
        average.append(calculate_average_activity(student_l, i))
    minimum = get_lowest_integer(average)
    if minimum is None:
        return None
    for i in range(len(average)):
        if minimum == average[i]:
            match i:
                case 0:
                    return 'Python'
                case 1:
                    return 'DSA'
                case 2:
                    return 'Databases'
                case 3:
                    return 'Flask'


def define_top_learners(student_l, course):
    match course:
        case 1:
            return sorted(student_l, key=cmp_to_key(lambda student1, student2: student1.python - student2.python),
                          reverse=True)
        case 2:
            return sorted(student_l, key=cmp_to_key(lambda student1, student2: student1.dsa - student2.dsa),
                          reverse=True)
        case 3:
            return sorted(student_l, key=cmp_to_key(lambda student1, student2: student1.databases - student2.databases),
                          reverse=True)
        case 4:
            return sorted(student_l, key=cmp_to_key(lambda student1, student2: student1.flask - student2.flask),
                          reverse=True)
    raise IndexError


def notify(student, course):
    title = ""
    match course:
        case 1:
            title = "Python"
        case 2:
            title = "DSA"
        case 3:
            title = "Databases"
        case 4:
            title = "Flask"

    msg = f"""To: {student.email}
Re: Your Learning Progress
Hello, {student.first_name} {student.last_name}! You have accomplished our {title} course!"""
    return msg


def main():
    print("Learning progress tracker")
    student_list = []
    python_activity = 0
    dsa_activity = 0
    databases_activity = 0
    flask_activity = 0

    while True:
        inp = input().strip()
        if inp == 'exit':
            print('Bye!')
            break
        match inp:
            case '':
                print('No input.')
            case 'back':
                print('Enter \'exit\' to exit the program')
            case 'add students':
                print('Enter student credentials \'first_name last_name email\' or \'back\' to return')
                student_count = 0
                while True:
                    student = input().split()
                    if len(student) != 0 and student[0] == 'back':
                        print(f'Total {student_count} students have been added.')
                        break
                    if len(student) < 3:
                        print('Incorrect credentials.')
                        continue

                    first_name = student[0]
                    last_name = ' '.join(student[1:len(student) - 1])
                    email = student[len(student) - 1]

                    if not check_name(first_name):
                        print('Incorrect first name.')
                        continue
                    if not check_name(last_name):
                        print('Incorrect last name.')
                        continue
                    if not check_email(email):
                        print('Incorrect email.')
                        continue
                    if email in [student.email for student in student_list]:
                        print('This email is already taken.')
                        continue

                    student_list.append(Student(first_name, last_name, email))
                    student_count += 1
                    print('The student has been added.')

            case 'list':
                if not student_list:
                    print('No students found')
                else:
                    print('Students:')
                    for student in student_list:
                        print(student.id)

            case 'add points':
                print('Enter an id and points \'id python dsa databases flask\' or \'back\' to return')
                while True:
                    points = input()
                    if points == 'back':
                        break
                    points = points.split()
                    try:
                        if len(points) != 5:
                            raise IndexError
                        if not points[0].isnumeric():
                            raise StringId
                        student_id = points[0]
                        python = points[1]
                        dsa = points[2]
                        databases = points[3]
                        flask = points[4]

                        if python.isdigit() and dsa.isdigit() and databases.isdigit() and flask.isdigit():
                            student_id = int(student_id)
                            python = int(python)
                            dsa = int(dsa)
                            databases = int(databases)
                            flask = int(flask)
                        else:
                            raise ValueError

                        if python < 0 or dsa < 0 or databases < 0 or flask < 0:
                            raise ValueError

                    except ValueError:
                        print('Incorrect points format.')
                        continue

                    except IndexError:
                        print('Incorrect points format.')
                        continue

                    except StringId:
                        print(f'No student is found for id={points[0]}')
                        continue

                    found = False
                    for student in student_list:
                        if student_id == student.id:
                            if python != 0:
                                student.python += python
                                python_activity += 1
                            if dsa != 0:
                                student.dsa += dsa
                                dsa_activity += 1
                            if databases != 0:
                                student.databases += databases
                                databases_activity += 1
                            if flask != 0:
                                student.flask += flask
                                flask_activity += 1
                            print('Points updated.')
                            found = True
                            break
                    if not found:
                        print(f'No student is found for id={student_id}')

            case 'find':
                print('Enter an id or \'back\' to return')
                while True:
                    find_inp = input()
                    if find_inp == 'back':
                        break
                    try:
                        student_id = int(find_inp)
                    except ValueError:
                        print(f'No student is found for id={find_inp}')
                        continue

                    found = False
                    for student in student_list:
                        if student_id == student.id:
                            print(
                                f'{student_id} points: Python={student.python}; '
                                f'DSA={student.dsa}; '
                                f'Databases={student.databases}; '
                                f'Flask={student.flask}')
                            found = True
                            break
                    if not found:
                        print(f'No student is found for id={find_inp}')
            case 'statistics':
                print('Type the name of a course \'python, dsa, databases, flask\' to see details or \'back\' to quit:')
                if not calculate_most_popular(student_list):
                    most_popular = 'n/a'
                    print(f'Most popular: {most_popular}')
                else:
                    most_popular = calculate_most_popular(student_list)
                    print(f"Most popular: {', '.join(most_popular)}")

                if not calculate_least_popular(student_list):
                    least_popular = 'n/a'
                    print(f'Least popular: {least_popular}')
                else:
                    least_popular = calculate_least_popular(student_list)
                    print(f"Least popular: {', '.join(least_popular)}")

                if not (python_activity and dsa_activity and databases_activity and flask_activity):
                    highest_activity = 'n/a'
                    print(f'Highest activity: {highest_activity}')
                else:
                    highest_activity = calculate_highest_activity(python_activity, dsa_activity, databases_activity,
                                                                  flask_activity)
                    print(f"Highest activity: {', '.join(highest_activity)}")

                if not calculate_lowest_activity(python_activity, dsa_activity, databases_activity, flask_activity):
                    lowest_activity = 'n/a'
                    print(f'Lowest activity: {lowest_activity}')
                else:
                    lowest_activity = calculate_lowest_activity(python_activity, dsa_activity, databases_activity,
                                                                flask_activity)
                    print(f'Lowest activity: {lowest_activity}')

                easiest = 'n/a' if not calculate_easiest_course(student_list) else calculate_easiest_course(
                    student_list)
                hardest = 'n/a' if not calculate_hardest_course(student_list) else calculate_hardest_course(
                    student_list)

                print(f'Easiest course: {easiest}')
                print(f'Hardest course: {hardest}')

                while True:
                    course = input()
                    if course == 'back':
                        break
                    match course:
                        case 'Python' | 'python':
                            print('Python\nid points completed')
                            sorted_list = define_top_learners(student_list, 1)
                            for student in sorted_list:
                                print(student.id, student.python,
                                      f'{round(student.python / 600 * 100, 1)}%')
                        case 'DSA' | 'dsa':
                            print('DSA\nid points completed')
                            sorted_list = define_top_learners(student_list, 2)
                            for student in sorted_list:
                                print(student.id, student.dsa,
                                      f'{round(student.dsa / 400 * 100, 1)}%')
                        case 'Databases' | 'databases':
                            print('Databases\nid points completed')
                            sorted_list = define_top_learners(student_list, 3)
                            for student in sorted_list:
                                print(student.id, student.databases,
                                      f'{round(student.databases / 480 * 100, 1)}%')
                        case 'Flask' | 'flask':
                            print('Flask\nid points completed')
                            sorted_list = define_top_learners(student_list, 4)
                            for student in sorted_list:
                                print(student.id, student.flask,
                                      f'{round(student.flask / 550 * 100, 1)}%')
                        case _:
                            print('Unknown course.')

            case 'notify':
                count_notify = 0
                for student in student_list:
                    student_notified = False
                    if not student.notified_python and student.python == 600:
                        student_notified = True
                        print(notify(student, 1))
                        student.notified_python = True
                    if not student.notified_dsa and student.dsa == 400:
                        student_notified = True
                        print(notify(student, 2))
                        student.notified_dsa = True
                    if not student.notified_databases and student.databases == 480:
                        student_notified = True
                        print(notify(student, 3))
                        student.notified_databases = True
                    if not student.notified_flask and student.flask == 550:
                        student_notified = True
                        print(notify(student, 4))
                        student.notified_flask = True
                    if student_notified:
                        count_notify += 1
                print(f'Total {count_notify} have been notified.')
            case 'help':
                print('Available functions: ' + ' | '.join(help_functions))
            case _:
                print('Error: unknown command. Hint: Type \'help\'')


main()
