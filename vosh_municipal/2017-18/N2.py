

def solve_n2_bad(n, m, presses):
    winds = []
    for i in range(n):
        winds.append(i+1)
    for press in presses:
        print(press)
        wind = winds[press%n]
        winds.remove(wind)
        winds.insert(0, wind)
    return winds.index(m)+1


def solve_n2(n, m, presses):
    cur_pos = m
    for press in presses:
        mv_wind = press % n + 1
        if mv_wind == cur_pos:
            cur_pos = 1
        elif mv_wind > cur_pos:
            cur_pos += 1
    return cur_pos


def main():
    n = int(input())
    m = int(input())
    k = int(input())
    presses = []
    for i in range(k):
        presses.append(int(input()))
    print(solve_n2(n, m, presses))


def test1():
    assert solve_n2(3, 2, [1, 5, 2]) == 3


def test2():
    assert solve_n2(5, 3, [2, 4, 9, 8]) == 4


def test_large():
    presses = []
    for i in range(100000):
        presses.append(5000)
    solve_n2(100000, 7, presses)


if __name__ == '__main__':
    #main()
    test1()
    test_large()