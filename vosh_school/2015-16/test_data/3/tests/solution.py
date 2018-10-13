m = int(input())
d = int(input())

while d <= 31:
    print(m, d)
    d += 7
    if m == 9 and d > 30:
        m = 10
        d -= 30
    if m == 10 and d > 31:
        m = 11
        d -= 31
    if m == 11 and d > 30:
        m = 12
        d -= 30
