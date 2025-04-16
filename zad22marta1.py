import time
import random

def gcd_subtraction(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        return gcd_subtraction(b, a)
    return gcd_subtraction(a - b, b)

def measure_time(func, a, b, iterations=100):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        func(a, b)
        end_time = time.time()
        total_time += (end_time - start_time)
    return total_time / iterations

numbers = [10, 100, 1000, 10000, 100000, 1000000]
results = []

for num in numbers:
    a = random.randint(1, num)
    b = random.randint(1, num)
    avg_time = measure_time(gcd_subtraction, a, b)
    results.append((num, avg_time))

print("Число\tСреднее время (сек)")
for num, time_taken in results:
    print(f"{num}\t{time_taken:.6f}")