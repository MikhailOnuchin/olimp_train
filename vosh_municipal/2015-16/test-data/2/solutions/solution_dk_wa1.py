N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
ans = N
num_A = 0
while num_A * A <= N:
    curr_cost = B * num_A
    remain = N - A * num_A
    num_C = remain // C
    curr_cost += num_C * D + remain % C
    ans = min(ans, curr_cost)
    num_A += 1
ans = min(ans, B * num_A)
print(ans)

