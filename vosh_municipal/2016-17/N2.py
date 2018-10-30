def shorter(a, b):
    a1 = a
    b1 = b
    while b != 0:
        a, b = b, a % b
    divider = a
    a = a1 // divider
    b = b1 // divider
    return a, b


def fract(a, b, c, d):
    i = 0
    while True:
        if a / b > c / d:
            return 0
        i += 1
        a += 1
        b += 1
        a, b = shorter(a, b)
        if a == c and b == d:
            return i


def test():
    assert fract(1, 60, 2, 63) == 0
    assert fract(3, 7, 1, 2) == 1
    assert fract(3, 59, 1, 2) == 8
    assert fract(2, 81, 5, 92) == 0
    assert fract(1, 24, 19, 43) == 0


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(fract(a, b, c, d))


#main()
test()