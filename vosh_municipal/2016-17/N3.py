import os


def proximity(gen1, gen2):
    digrams1 = {}
    digrams2 = {}
    for i in range(len(gen1)-1):
        digram = gen1[i:i + 2]
        if digram not in digrams1.keys():
            digrams1[digram] = 1
        else:
            digrams1[digram] += 1
    for i in range(len(gen2)-1):
        digram = gen2[i:i + 2]
        if digram not in digrams2.keys():
            digrams2[digram] = 1
        else:
            digrams2[digram] += 1
    ans = 0
    for digram in digrams1.keys():
        if digram in digrams2.keys():
            ans += digrams1[digram]
    return ans


def test():
    assert proximity('ABBACAB', 'BCABB') == 4
    assert proximity('ABBA', 'CDDDC') == 0
    assert proximity('AAAAAAA', 'AAB') == 6
    assert proximity('AAAAAAA', 'AAAB') == 6
    assert proximity('COSGPLOWDYWVODEELOFHAYAUZPJBQLXCLXBTQLYCXBHLIDNPAVBEAHCVOAZCN',
                 'LEOQXASTXXECCFZVXOJKZPGGCMSQVBITNAQBWKHGFGRXRCIXJBHPVQLDOXFDTMWDEYTSZQNTJHXWMFBRNC') == 8


def slow_test():
    import time
    t = time.monotonic()
    assert proximity('A'*100000, 'B'*100000) == 0
    assert proximity('ABCDEFGHIJ'*10000, 'FGHIJKLMNO'*10000) == 40000
    d = time.monotonic() - t
    print(d)
    assert d <= 2


def auto_test():
    rel_dir = 'test-data/3/tests'
    for fn in os.listdir(rel_dir):
        if fn.endswith(".a"):
            test_params = open(rel_dir + '/' + fn[:-2], 'r').readlines()
            expected = int(open(rel_dir + '/' + fn, 'r').read())
            ans = proximity(test_params[0].strip(), test_params[1].strip())
            if ans != expected:
                print('%s: %s not equal to %s' % (fn, expected, ans))


def main():
    gen1 = input()
    gen2 = input()
    ans = proximity(gen1, gen2)
    print(ans)


#auto_test()
#test()
slow_test()