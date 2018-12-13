

n = int(input())
ans = 1
d = 1
while n >= 2 * d:
    d *= 2
    ans += 1
print(ans)
