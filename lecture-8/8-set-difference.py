''' Difference of A and B (A - B) is a set of elements that are only in A but not in B
    Similiarly, B - A is a set of elements in B but not in A
    
    Difference is performed using - operator. Same can be accomplished using the method
    difference().   '''

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)
