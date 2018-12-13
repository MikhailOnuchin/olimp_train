#include <iostream>
#include <vector>

using namespace std;

vector<int> x;
int passed, n;

int show(vector<int> &x) {
    for (int i = 0; i < x.size(); i++) {
        cout << x[i] << " ";
    }
}

int solution_9_11_4_TL(vector<int> &x) {
    int passed, sz, i, mx;
    n = x.size();
    passed = 0;
    while (x[n - 1] > passed + 1) {
        i = n - 1;
        x[i] -= 1;
        passed += 1;
        while ((x[n - 1] > passed) && (i > 0) && (x[i - 1] > x[i])) {
            x[--i] -= 1;
            passed += 1;
        }
//        show(x);
//        cout << "\n";
    }
    i = n - 1;
    mx = x[i];
    while ((i > 0) && (x[i - 1] == x[i])) {
        i -= 1;
    }
    if ((i > 0) && (x[i - 1] > mx)) {
        return(x[i - 1]);
    }
    else {
        return mx;
    }
}

int main() {
    int t;
    cin >> n;
    x.resize(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> x[i];
    }
    cout << solution_9_11_4_TL((x));
}
