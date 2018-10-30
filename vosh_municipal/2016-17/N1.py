

def elect(n, k):
    n = n // 2 + 1
    k = k // 2 + 1
    return n * k


def test():
    assert elect(5, 3) == 6
    assert elect(1, 1) == 1
    assert elect(9, 13) == 35
    assert elect(2, 2) == 4


def main():
    n = int(input())
    k = int(input())
    print(elect(n, k))


test()
#main()