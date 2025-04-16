def factorial_mod_p(N, P):
    if N >= P:
        return 0
    result = 1
    while N > 0:
        for i in range(1, N + 1):
            if i % P != 0:
                result = (result * i) % P
        N //= P
    return result
N = int(input())
P = int(input())
print(factorial_mod_p(N,P ))