import time


def benchmarkable_function():
    result = 0
    for i in range(100):
        result += 2
    time.sleep(3)
    return result
