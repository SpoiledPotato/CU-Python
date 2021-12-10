def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i]/float(L2[i]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))  # NaN = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios


list1 = [10, 20]
list2 = [2, 'a']

print(get_ratios(list1, list2))
