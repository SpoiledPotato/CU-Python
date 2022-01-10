import psutil

def rand():
    cpuCount = int(16 / psutil.cpu_count())
    binary = ""
    for i in range(cpuCount):
        for el in psutil.cpu_percent(interval=0.2, percpu=True):
            binary += str(int(el % 2))
            print(el)

    return(int(binary, 2))


print(rand())
