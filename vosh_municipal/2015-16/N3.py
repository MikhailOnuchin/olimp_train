import os


def alg(n):
    if len(n) == 4:
        first = int(n[:2])
        last = int(n[2:])
        if first < last or first > 18 or last > 18:
            return 0
        else:
            if first > last:
                first, last = last, first
            a = first - 9
            b = 9
            c = last - 9
            d = 9
    elif len(n) == 3:
        first = int(n[:2])
        last = int(n[2:])
        if first > 18:
            return 0
        a = first - 9
        b = 9
        c = 0
        d = 0
        if last != 0:
            d = last - 1
            c = 1
            if a > c or (a == c and b > d):
                a, b, c, d = c, d, a, b
    elif len(n) == 2:
        first = int(n[0])
        last = int(n[1])
        if first < last:
            return 0
        a = 1
        b = 0
        c = 0
        d = 0
        if last != 0:
            b = last -1
            d = first
        else:
            b = first - 1
            d = last
    return int(str(a) + str(b) + str(c) + str(d))


def test():
    assert alg('1311') == 2949
    assert alg('89') == 0
    assert alg('157') == 1669
    assert alg('189') == 1899
    assert alg('1735') == 0
    assert alg('1713') == 4989
    assert alg('101') == 1019


def auto_test():
    rel_dir = 'test-data/3/tests'
    for fn in os.listdir(rel_dir):
        if fn.endswith(".a"):
            test_params = list(map(int, open(rel_dir + '/' + fn[:-2], 'r').readlines()))
            expected = list(map(int, open(rel_dir + '/' + fn, 'r').read().split()))
            ans = alg(str(test_params[0]))
            if ans != expected[0]:
                print('%s: %s not equal to %s' % (fn, str(expected[0]), ans))



def main():
    n = input()
    k = alg(n)
    print(k)


auto_test()