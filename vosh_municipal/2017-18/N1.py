

a = int(input())
b = int(input())
c = int(input())
first = ((a + c - 1)//c)*c
last = (b//c)*c
print((last-first)//c + 1)