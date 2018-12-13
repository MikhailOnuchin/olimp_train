N = int(input())
V = N % 4
N //= 4
P = N % 4
N //= 4
A = N % 3
S = N // 3
print(S, A, P, V)

