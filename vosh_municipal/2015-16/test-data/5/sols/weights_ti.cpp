#include <cmath>
#include <cstdio>

int main() {
    int n;
    scanf("%d", &n);
    
    int answer = ceil(log(n) / log(3.)), curr = 2;
    for (int i = 0; i != answer; ++i) {
        printf("%d ", curr);
        curr *= 3;
    }
    printf("\n");
    
    return 0;
}
