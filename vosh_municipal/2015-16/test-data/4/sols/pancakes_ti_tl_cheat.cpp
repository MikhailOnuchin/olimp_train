#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

bool check(vector<int> const &pancakes, int to_check) {
    long long lack_sum = 0;
    
    for (vector<int>::const_iterator it = pancakes.begin(); it != pancakes.end(); ++it) {
        if (*it > to_check) {
            lack_sum += *it - to_check;
        }
    }
    
    return lack_sum <= to_check;
}

int solve(vector<int> const &pancakes, int max) {
    for (; check(pancakes, max); --max);
    return max + 1;
}


int main() {
    int n;
    cin >> n;
    
    vector<int> pancakes(n);
    for (int i = 0; i != n; ++i) {
        cin >> pancakes[i];
    }
    
    int max_val = *max_element(pancakes.begin(), pancakes.end());
    
    if (check(pancakes, max_val / 2)) {
        max_val /= 2;
    }
    
    cout << solve(pancakes, max_val) << '\n';
    return 0;
}
