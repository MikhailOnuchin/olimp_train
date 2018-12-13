def solution_OK(N, A, B, C, D):
	res = N
	for x in range((N + A - 1) // A + 1):

		if x * A < N:
			y = (N - x * A) // C
		else:
			y = 0

		if N - x * A - y * C > 0:
			z = N - x * A - y * C
		else:
			z = 0

		if res > min(x * B + y * D + z, x * B + (y + 1) * D):
			res = min(x * B + y * D + z, x * B + (y + 1) * D)
	return res

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
print(solution_OK(N, A, B, C, D))
