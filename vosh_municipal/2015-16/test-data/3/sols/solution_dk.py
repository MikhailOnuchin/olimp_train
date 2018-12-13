n = input()
for k in range(1000, 10000):
    digits = list(map(int, str(k)))
    a = [digits[0] + digits[1], digits[2] + digits[3]]
    a.sort(reverse=True)
    if n == "".join(map(str, a)):
        print(k)
        break
else:
    print(0)
