#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int n, s, a, p, v;

int main()
{
    cin >> n;
    s = 0;
    a = 0;
    p = 0;
    v = 0;

    while (n >= 48) {
        n -= 48;
        s ++;
    }
    while (n >= 16) {
        n -= 16;
        a ++;
    }
    while (n >= 4) {
        n -= 4;
        p ++;
    }
    v = n;
    cout << s << " " << a << " " << p << " " << v;
}
