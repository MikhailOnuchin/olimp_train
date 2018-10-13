n = int(input())
ans = 1
p = 1
while 2 * p <= n:
    p *= 2
    ans += 1
print(ans)


