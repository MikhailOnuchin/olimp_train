n, a, b, c, d = [int(input()) for i in range(5)]

def f(n, c, d):
    ans = n // c * d
    n %= c
    ans += min(n, d)
    return ans

print(min(f(n, a, b), f(n, c, d)))


