#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int weights[1000000 + 10];
char covered[1000000 + 10];

int N, ANSWER = 1;

void Print() {
    for (int i = 0; i != ANSWER; ++i) {
        printf("%d ", weights[i]);
    }
    printf("\n");
    exit(0);
}

void CountSum(int idx, int sum) {
    if (idx == ANSWER) {
        if (sum >= 1 && sum <= N) {
            covered[sum - 1] = 1;
        }
        return;
    }
    
    CountSum(idx + 1, sum);
    CountSum(idx + 1, sum - weights[idx]);
    CountSum(idx + 1, sum + weights[idx]);
}

char Check() {
    memset(covered, 0, N);
    CountSum(0, 0);
    for (int i = 0; i != N - 1; ++i) {
        if (!covered[i] && !covered[i + 1]) {
            return 0;
        }
    }
    return 1;
}

void BruteForce(int idx, int last) {
    if (idx == ANSWER) {
        if (Check()) {
            Print();
        }
        
        return;
    }
    
    for (weights[idx] = last; weights[idx] <= N; ++weights[idx]) {
        BruteForce(idx + 1, weights[idx]);
    }
}

void Solve(int n) {
    N = n;
    ANSWER = ceil(log(n) / log(3.));
    
    BruteForce(0, 1);
}

int main(int argc, char **argv) {
    int n;
    scanf("%d", &n);
    Solve(n);
    
    return 0;
}
