n = int(input())
p = int(input())
k = int(input())
ans1 = p - 1
ans2 = p + 1
if p % 2 == 1:
    ans1 += 2 * k
    ans2 += 2 * k
else:
    ans1 -= 2 * k
    ans2 -= 2 * k
ans1 %= n
ans2 %= n
if ans1 == 0:
    ans1 = n
if ans2 == 0:
    ans2 = n
print(min(ans1, ans2), max(ans1, ans2))

