# Ручка стоила K рублей. Первого сентября стоимость ручки увеличилась ровно на P процентов. Определите, сколько ручек
# можно купить на S рублей после подорожания


k = int(input())
p = int(input())
s = 100 * int(input())
k = k * (100+p)
print(s // k)