# Дано число. В этом числе необходимо изменить одну цифру таким образом, чтобы новое число делилось на 3 и было бы
# максимально возможным. В исходном числе нужно обязательно изменить одну цифру, даже если исходное число уже делилось на 3


my_int = input()
digits = []
digit_sum = 0
for digit in my_int:
    digit_sum += int(digit)
    digits.append(int(digit))
addendum = 3 - (digit_sum % 3)
found = False
for i in range(len(digits)):
    new_digit = digits[i] + addendum
    if new_digit > 9:
        continue
    else:
        found = True
        digits[i] = new_digit
        break
if not found:
    assert digits[-1] > 6
    if digit_sum % 3 == 0:
        digits[-1] -= 3
    else:
        digits[-1] -= digit_sum % 3
for digit in digits:
    print(digit, end='')