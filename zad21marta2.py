import numpy as np
import time
import matplotlib.pyplot as plt

def intersection_set(lst1, lst2):
    return list(set(lst1) & set(lst2))

def intersection_naive(lst1, lst2):
    result = []
    for item in lst1:
        if item in lst2 and item not in result:
            result.append(item)
    return result

def measure_time(func, lst1, lst2, repeats=5):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.time()
        result = func(lst1, lst2)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, np.mean(times)

sizes = [10, 100, 500, 1000, 2000, 5000]
times_set = []
times_naive = []

for size in sizes:
    arr1 = list(np.random.randint(0, size * 2, size))
    arr2 = list(np.random.randint(0, size * 2, size))

    result_set, time_set = measure_time(intersection_set, arr1, arr2)
    times_set.append(time_set)

    result_naive, time_naive = measure_time(intersection_naive, arr1, arr2)
    times_naive.append(time_naive)

    print(f"Размер: {size:>6} | Множества: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

plt.figure(figsize=(12, 7))
plt.plot(sizes, times_set, label="Множества (O(n + m))", marker="o", color="green")
plt.plot(sizes, times_naive, label="Наивный способ (O(n * m))", marker="s", color="red")

plt.title("Сравнение времени нахождения пересечения списков")
plt.xlabel("Размер списков")
plt.ylabel("Время выполнения (секунды)")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()
