def my_function(x):
    return list(dict.fromkeys(x))


mylist = my_function(['a', 'b', 'a', 'c', 'c'])
print(mylist)


a = [5, 6, 5, 6, 7, 8]
print(list(set(a)))
