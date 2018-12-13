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

int main() {
    int n;
    cin >> n;
    
    vector<int> pancakes(n);
    for (int i = 0; i != n; ++i) {
        cin >> pancakes[i];
    }
    
    int left = 0, right = *max_element(pancakes.begin(), pancakes.end());
    
    while (left + 1 != right) {
        int middle = left + (right - left) / 2;
        
        if (check(pancakes, middle)) {
            right = middle;
        } else {
            left = middle;
        }
    }
    
    cout << right << '\n';
    return 0;
}
