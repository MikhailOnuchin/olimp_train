

n = int(input())
mountains = []
for i in range(n):
    mountains.append(int(input()))
start = -1
end = -1
best_start = -1
best_end = -1
for i in range(1, n):
    if mountains[i] > mountains[i-1]:
        start = i
    if mountains[i] < mountains[i-1]:
        end = i + 1
    if start != -1 and end != -1:
        if end > start:
            if best_start == -1 and best_end == -1:
                best_start = start
                best_end = end
            else:
                if best_end - best_start > end - start:
                    best_start = start
                    best_end = end
if best_start == -1 and best_end == -1:
    print(0)
else:
    print(best_start)
    print(best_end)