names = ['Ana', 'John', 'Denise', 'Katy']
grade = ['B', 'A+', 'A', 'A']
course = [2.00, 6.0001, 20.002, 9.01]

def getStudentInfo(name):
    i = names.index(name)
    return grade[i], course[i]

print(getStudentInfo('John'))