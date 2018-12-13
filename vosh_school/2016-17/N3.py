

s = int(input())
n = int(input())
bp_weight = 0
sc_weght = 0
for i in range(n):
    stuff = int(input())
    if stuff <= s - bp_weight:
        bp_weight += stuff
    else:
        sc_weght += stuff
print(bp_weight)
print(sc_weght)