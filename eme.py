name_grades = {}

while True:
    name = input("Please give me the name of the student [q to quit]:")
    if name == 'q':
        break
    else:
        grade = input("Give me their grade: ")
        name_grades[name]=grade
        print(name_grades)