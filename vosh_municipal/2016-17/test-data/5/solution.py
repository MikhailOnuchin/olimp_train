n = int(input())
a = [int(input()) for i in range(n)]
i = 0
j = 0
while j < n:
    if a[i] != 0:
        print(a[i])
        while a[j] != a[i] // 3 * 4:
            j += 1
        a[j] = 0
        j += 1
    i += 1
