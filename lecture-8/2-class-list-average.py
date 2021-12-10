def avg(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return(0.0)


def new_stats(class_list):
    new_list = []
    for el in class_list:
        new_list.append([el[0], el[1], avg(el[1])])
    return new_list


test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
               [['bruce', 'wayne'], [100.0, 80.0, 74.0]]]

print(new_stats(test_grades))
