n = int(input())

min1 = 40001
min2 = 40001
max1 = -40001
max2 = -40001

for i in range(n):
    x = int(input())
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2:
        max2 = x
    if x < min1:
        min2 = min1
        min1 = x
    elif x < min2:
        min2 = x

print(min(min1 * max1, min1 * min2, max1 * max2))
