import numpy as np
import time
import matplotlib.pyplot as plt

def first_repeating_set(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return item
        seen.add(item)
    return None

def first_repeating_no_set(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return lst[i]
    return None

def measure_time(func, lst, repeats=5):
    times = []
    result = None
    for _ in range(repeats):
        start_time = time.time()
        result = func(lst)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, np.mean(times)

sizes = [10, 100, 500, 1000, 2000, 5000]
times_set = []
times_naive = []

for size in sizes:
    arr = list(np.random.randint(0, size * 2, size))

    result_set, time_set = measure_time(first_repeating_set, arr)
    times_set.append(time_set)

    result_naive, time_naive = measure_time(first_repeating_no_set, arr)
    times_naive.append(time_naive)

    print(f"Размер: {size:>6} | Множества: {time_set:.6f}s | Наивный метод: {time_naive:.6f}s")

plt.figure(figsize=(12, 7))
plt.plot(sizes, times_set, label="Множества (O(n))", marker="o", color="green")
plt.plot(sizes, times_naive, label="Наивный способ (O(n^2))", marker="s", color="red")

plt.title("Сравнение времени нахождения первого повторяющегося элемента")
plt.xlabel("Размер списка")
plt.ylabel("Время выполнения (секунды)")
plt.grid(True, which="both", linestyle="--")
plt.legend()
plt.show()
