import os


def prices(n, all_prices):
    ans = []
    for i in range(n//2):
        new_price = all_prices[0]
        ans.append(new_price)
        all_prices.remove(new_price)
        all_prices.remove(new_price//3*4)
    return ans


def test():
    assert prices(6, [30, 40, 42, 45, 56, 60]) == [30, 42, 45]


def auto_test():
    rel_dir = 'test-data/5/tests'
    for fn in os.listdir(rel_dir):
        if fn.endswith(".a"):
            test_params = list(map(int, open(rel_dir + '/' + fn[:-2], 'r').readlines()))
            expected = list(map(int, open(rel_dir + '/' + fn, 'r').read().split()))
            ans = prices(test_params[0], test_params[1:])
            print(fn)
            if ans != expected:
                print('%s: %s not equal to %s' % (fn, expected, ans))



def main():
    n = int(input())
    all_prices = []
    for i in range(n):
        all_prices.append(int(input()))
    ans = prices(n, all_prices)
    for price in ans:
        print(price)


test()
auto_test()