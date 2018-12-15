import os


def mts(targ, plans):
    ans = 0
    if len(plans) == 1:
        return targ
    cur_plan = plans[0][0]
    cur_price = plans[0][1]
    n = targ // cur_plan
    ans += cur_price * n
    targ %= cur_plan
    if targ != 0:
        another_price = mts(targ, plans[1:])
        if another_price < cur_price:
            ans += another_price
        else:
            ans += cur_price
    return ans


def auto_test():
    rel_dir = 'test-data/2/tests'
    for fn in os.listdir(rel_dir):
        if fn.endswith(".a"):
            test_params = list(map(int, open(rel_dir + '/' + fn[:-2], 'r').readlines()))
            targ = test_params[0]
            plans = []
            plan1 = test_params[1]
            price1 = test_params[2]
            plan2 = test_params[3]
            price2 = test_params[4]
            if plan1 * price2 < plan2 * price1:
                plan1, plan2 = plan2, plan1
                price1, price2 = price2, price1
            plans.append([plan1, price1])
            plans.append([plan2, price2])
            plans.append([1, 1])

            expected = list(map(int, open(rel_dir + '/' + fn, 'r').read().split()))
            ans = mts(targ, plans)
            if ans != expected[0]:
                print('%s: %s not equal to %s' % (fn, str(expected[0]), ans))


def main():
    targ = int(input())
    plans = []
    plan1 = int(input())
    price1 = int(input())
    plan2 = int(input())
    price2 = int(input())
    if plan1*price2 < plan2*price1:
        plan1, plan2 = plan2, plan1
        price1, price2 = price2, price1
    plans.append([plan1, price1])
    plans.append([plan2, price2])
    plans.append([1, 1])
    ans = mts(targ, plans)
    print(ans)


auto_test()