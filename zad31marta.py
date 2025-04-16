import time
import matplotlib.pyplot as plt


def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True

    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


def measure_time(n):
    start_time = time.time()
    is_perfect_square(n)
    end_time = time.time()
    return end_time - start_time


# Тестирование алгоритма
test_numbers = [9, 16, 25, 100, 10000, 1000000, 100000000]
for num in test_numbers:
    print(f"Число {num} явл полным квадратом: {is_perfect_square(num)}")

# Построение графика
input_sizes = [10 ** i for i in range(1, 8)]
times = [measure_time(n) for n in input_sizes]

plt.plot(input_sizes, times, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Размер входных данных (n)')
plt.ylabel('Время выполнения (seconds)')
plt.title('Зависимость времени проверки квадрата от размера числа')
plt.grid(True)
plt.show()