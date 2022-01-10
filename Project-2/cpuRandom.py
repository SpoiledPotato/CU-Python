import psutil


def random():
    percents = []
    generatedBinary = ""

    for _ in range(16//psutil.cpu_count()):
        percents.extend(psutil.cpu_percent(interval=0.1, percpu=True))

    for percent in percents:
        if percent > 4:
            generatedBinary += '1'
        else:
            generatedBinary += '0'

    decimal = 0
    for i in range(len(generatedBinary)):
        decimal += int(generatedBinary[-i-1]) * (2 ** i)

    return decimal


print(random())
