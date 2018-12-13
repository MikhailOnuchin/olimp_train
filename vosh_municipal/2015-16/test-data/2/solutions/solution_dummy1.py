n, a, b, c, d = [int(input()) for i in range(5)]
ans = n // a * b
n %= a
ans += min(n, b)
print(ans)

