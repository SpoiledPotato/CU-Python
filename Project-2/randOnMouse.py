import psutil

for _ in range(16):
    var = psutil.cpu_percent(interval=0.01)
    print(var)
    if var > 20:
        print(1, end='')
    else:
        print(0, end='')
