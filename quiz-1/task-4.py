l = {1: 1, 2: 1}
def fib_efficient(n):
    global l
    if n in l:
        return l[n]
    else:
        ans = fib_efficient(n-1) + fib_efficient(n-2)
        l[n] = ans
        return ans

months = 7

a = open("task-4.txt", 'w')
a.write(str(fib_efficient(months)))
a.close()