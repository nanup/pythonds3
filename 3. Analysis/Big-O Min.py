import time
import random

def nsquaredmin(a_list):
    overall_min = a_list[0]
    for i in a_list:
        is_min = True
        if i > overall_min: is_min = False
        if is_min:
            for j in a_list:
                if i > j: overall_min = j
    return overall_min

def nmin(a_list):
    overall_min = a_list[0]
    for i in a_list:
        if i < overall_min:
            overall_min = i
    return overall_min

for size in range(1000, 10001, 1000):
    a_list = [random.randrange(1000) for x in range(size)]
    start = time.time()
    nsquaredmin(a_list)
    end = time.time()
    print(f"{end - start:.5f}")

for size in range(1000, 10001, 1000):
    a_list = [random.randrange(1000) for x in range(size)]
    start = time.time()
    nmin(a_list)
    end = time.time()
    print(f"{end - start:.5f}")