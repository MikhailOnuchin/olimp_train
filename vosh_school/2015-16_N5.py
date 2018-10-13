# Дана последовательность из N целых чисел (они могут быть положительными, отрицательными или равными 0). Необходимо
# выбрать из этих чисел два числа так, чтобы их произведение было как можно меньшим (не рассматриваются квадраты данных
# чисел, но можно выбрать произведение двух различных элементов последовательности, равных друг другу).


n = int(input())
ints = []
for i in range(n):
    ints.append(int(input()))
min_mult = None
for pos1 in range(n):
    for pos2 in range(n):
        if pos1 == pos2:
            continue
        new_mult = ints[pos1] * ints[pos2]
        if min_mult == None:
            min_mult = new_mult
        if min_mult > new_mult:
            min_mult = new_mult
print(min_mult)