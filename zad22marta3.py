import time
import random
import math

def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n = n // i
        i += 2
    if n > 2:
        factors[n] = 1
    return factors

def gcd_prime_factors(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)
    common_factors = {}
    for factor in factors_a:
        if factor in factors_b:
            common_factors[factor] = min(factors_a[factor], factors_b[factor])
    result = 1
    for factor in common_factors:
        result *= factor ** common_factors[factor]
    return result

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
    avg_time = measure_time(gcd_prime_factors, a, b)
    results.append((num, avg_time))

print("Число\tСреднее время (сек)")
for num, time_taken in results:
    print(f"{num}\t{time_taken:.6f}")