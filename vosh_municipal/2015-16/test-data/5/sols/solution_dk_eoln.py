n = int(input())
s = 2
ans = [2]
while sum(ans) + 1 < n:
    ans.append(3 * ans[-1])
if n == 5:
    ans = [3, 4]
print(" ".join(map(str, ans)))

