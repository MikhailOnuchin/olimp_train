#include "testlib.h"
#include <vector>
#include <algorithm>

using namespace std;

bool check(const vector<int> & a, int i, int j)
{
    if (i == 0 && j == 0)
        return true;
    if (i == 0)
        return false;
    if (j <= i + 1)
        return false;
    int m = *max_element(a.begin() + i - 1, a.begin() + j);
    return m > a[i - 1] && m > a[j - 1];
}

int main(int argc, char **argv) {
    registerTestlibCmd(argc, argv);

    int n = inf.readInt(1, 100000);
    vector<int> a(n);
    for (int i = 0; i < n; ++i)
        a[i] = inf.readInt(1, 100000);
    int user_ans_1 = 0, user_ans_2 = 0, corr_ans_1 = 0, corr_ans_2 = 0;
    user_ans_1 = ouf.readInt(0, n);
    if (user_ans_1)
    {
        user_ans_2 = ouf.readInt(1, n);
        if (user_ans_2 <= user_ans_1)
            quitf(_wa, "First number must be less than second number");
    }
    if (!check(a, user_ans_1, user_ans_2))
        quitf(_wa, "User answer is incorrect");
    corr_ans_1 = ans.readInt(0, n);
    if (corr_ans_1)
    {
        corr_ans_2 = ans.readInt(1, n);
        if (corr_ans_2 <= corr_ans_1)
            quitf(_fail, "First number must be less than second number");
    }
    if (!check(a, corr_ans_1, corr_ans_2))
        quitf(_fail, "Jury answer is incorrect");
    if (user_ans_1 == 0 && corr_ans_1 == 0)
        quitf(_ok, "OK - no solution");
    if (user_ans_1 == 0)
        quitf(_wa, "Program output 0, but solution exists");
    if (corr_ans_1 == 0)
        quitf(_fail, "Jury output 0, but solution exists");
    if (user_ans_2 - user_ans_1 == corr_ans_2 - corr_ans_1)
        quitf(_ok, "OK - best answer");
    if (user_ans_2 - user_ans_1 > corr_ans_2 - corr_ans_1)
        quitf(_wa, "It isn't the best answer");
    if (user_ans_2 - user_ans_1 < corr_ans_2 - corr_ans_1)
        quitf(_fail, "User answer better than jury answer");


}

