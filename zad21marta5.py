import numpy as np
import time
import matplotlib.pyplot as plt

def two_sum_set(lst, target):
    seen = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None

def two_sum_no_set(lst, target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return (lst[i], lst[j])
    return None

def measure_time(func, lst, target, repeats=5):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.time()
        result = func(lst, target)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, np.mean(times)

sizes = [10, 100, 500, 1000, 2000, 5000]
times_set = []
times_naive = []

for size in sizes:
    arr = list(np.random.randint(0, size * 2, size))
    target = np.random.randint(0, size * 2)

    result_set, time_set = measure_time(two_sum_set, arr, target)
    times_set.append(time_set)

    result_naive, time_naive = measure_time(two_sum_no_set, arr, target)
    times_naive.append(time_naive)

    print(f"Размер: {size:>6} | Множества: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

plt.figure(figsize=(12, 7))
plt.plot(sizes, times_set, label="Множества (O(n))", marker="o", color="green")
plt.plot(sizes, times_naive, label="Наивный способ (O(n^2))", marker="s", color="red")

plt.title("Сравнение времени нахождения двух чисел, сумма которых равна целевому значению")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()
