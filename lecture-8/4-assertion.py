def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)

# raises an AssertionError if it i sgiven an empty list for grades
# otherwise runs ok