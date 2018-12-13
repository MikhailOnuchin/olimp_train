#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n;
int const MAX_WEIGHT = 1000 * 1000;

int weights[1000];
char covered[1000];

int ANSWER, N;

void Print() {
    if (n == N++) {
        for (int i = 0; i != ANSWER; ++i) {
            printf("%d ", weights[i]);
        }
        printf("\n");
        exit(0);
    }
}

void CountSum(int idx, int sum) {
    if (idx == ANSWER) {
        if (sum >= 1 && sum <= N) {
            covered[sum] = 1;
        }
        return;
    }
    
    CountSum(idx + 1, sum);
    CountSum(idx + 1, sum - weights[idx]);
    CountSum(idx + 1, sum + weights[idx]);
}

char Check() {
    memset(covered, 0, N + 2);
    CountSum(0, 0);
    for (int i = 1; i != N; ++i) {
        if (!covered[i] && !covered[i + 1]) {
            return 0;
        }
    }
    return 1;
}

void BruteForce(int idx, int last) {
    if (idx == ANSWER) {
        while (Check()) {
            Print();
        }
        return;
    }
    
    for (weights[idx] = last; weights[idx] <= N; ++weights[idx]) {
        BruteForce(idx + 1, weights[idx]);
    }
}

void Solve() {
    N = 1;
    
    for (ANSWER = 1; ; ++ANSWER) {
        BruteForce(0, 1);
    }
}

int main(int argc, char **argv) {
    scanf("%d", &n);
    Solve();
    
    return 0;
}
