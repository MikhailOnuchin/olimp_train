#include <iostream>

using namespace std;

int n, a, b, c, d;

int solution_TL(int N, int A, int B, int C, int D) {
    int res;
	res = N;
	for (int i=0; i <= N / A + 2; i++) {
			for (int j=0; j < N / C + 2; j++) {
                for (int k=0; k < N + 1; k++) {
                    if (res > i * B + j * D + k and i * A + j * C + k >= N) {
                        res = i * B + j * D + k;
                    }
                }
			}
	}
	return(res);
}

int main() {
    cin >> n;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;
    cout << solution_TL(n, a, b, c, d);
}
