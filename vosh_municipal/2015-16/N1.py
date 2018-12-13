

def resize(n):
    s = n // 48
    n %= 48
    a = n // 16
    n %= 16
    p = n // 4
    v = n % 4
    return s, a, p, v


def main():
    n = int(input())
    s, a, p, v = resize(n)
    print(s, a, p, v, sep=' ')


main()
