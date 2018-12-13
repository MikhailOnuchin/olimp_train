n, a, b, c, d = [int(input()) for i in range(5)]
ans = n // c * d
n %= c
ans += min(n, d)
print(ans)

