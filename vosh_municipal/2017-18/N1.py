

a = int(input())
b = int(input())
c = int(input())
ans = 0
for year in range(a, b+1):
    if year % c == 0:
        ans += 1
print(ans)