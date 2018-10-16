

n = int(input())
m = int(input())
k = int(input())
presses = []
for i in range(k):
    presses.append(int(input()))
winds = []
for i in range(n):
    winds.append(i+1)
for press in presses:
    wind = winds[press%n]
    winds.remove(wind)
    winds.insert(0, wind)
print(winds.index(m)+1)
