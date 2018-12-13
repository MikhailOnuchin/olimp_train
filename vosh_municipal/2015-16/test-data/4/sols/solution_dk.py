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
    m = (sum + count - 1) // count
    if a[i - 1] <= m <= a[i] and m < ans:
        ans = m
print(ans)
