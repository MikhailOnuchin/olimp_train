n = int(input())
m = int(input())
k = int(input())
for i in range(k):
    t = int(input()) % n
    if 1 + t > m:
        m += 1
    elif 1 + t == m:
        m = 1
print(m)


