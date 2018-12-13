n = int(input())
a = [0]
for i in range(n):
    a.append(int(input()))
ans = a[-1]
sum = 0
count = 1
for i in range(n, 0, -1):
    sum += a[i]
    count += 1
    ans = min(ans, max(a[i - 1], (sum + count - 1) // count))
print(ans)

