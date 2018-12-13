N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
ans = N
num_C = 0
while num_C * C <= N:
    curr_cost = D * num_C
    remain = N - C * num_C
    num_A = remain // A
    curr_cost += num_A * B + remain % A
    ans = min(ans, curr_cost)
    num_C += 1
ans = min(ans, C * num_C)
print(ans)

