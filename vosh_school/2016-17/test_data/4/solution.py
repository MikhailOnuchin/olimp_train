n = int(input())
ans1 = 0
ans2 = 0
last_height = 10 ** 9
prev_height = 10 ** 9
last_len = 0
best_len = 10 ** 9
for i in range(1, n + 1):
    h = int(input())
    if h == last_height:
        last_len += 1
    else:
        if prev_height < last_height > h and last_len < best_len:
            best_len = last_len
            ans1 = i - last_len - 1
            ans2 = i
        prev_height = last_height
        last_height = h
        last_len = 1
if ans1 == 0:
    print(0)
else:
    print(ans1, ans2)
