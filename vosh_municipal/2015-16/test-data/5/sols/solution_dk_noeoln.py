import sys
n = int(input())
s = 2
ans = [2]
while sum(ans) + 1 < n:
    ans.append(3 * ans[-1])
sys.stdout.write(" ".join(map(str, ans)))
