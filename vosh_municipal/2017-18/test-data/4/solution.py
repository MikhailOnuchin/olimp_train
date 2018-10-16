k = int(input())
n = int(input())
a = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = int(input())
ans = 0
free = 0
for i in range(n, 0, -1):
    if a[i] <= free:
        free -= a[i]
    else:
        a[i] -= free
        num = (a[i] + k - 1) // k
        ans += 2 * num * i
        free = num * k - a[i]
print(ans)

