def solution_OK(x):
	# if len(x) == 1:
	# 	return len(x) // 2 + len(x) % 2
	passed = 0
	i = len(x) - 1
	length = 1
	while i - 1 >= 0 and x[i - 1] == x[i]:
		i -= 1
		length += 1
	while length < x[-1] - passed:
		to_pass = (x[i] - passed) // (length + 1)
		if i > 0 and x[i] - to_pass < x[i - 1]:
			to_pass = (x[i] - x[i - 1])
		passed += to_pass * length
		for j in range(i, i + length):
			x[j] -= to_pass
		while i - 1 >= 0 and x[i - 1] == x[i]:
			i -= 1
			length += 1
	return x[i]


n = int(input())
x = []
for i in range(n):
	x.append(int(input()))

print(solution_OK(x))
