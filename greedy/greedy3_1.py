#거스름돈 문제
n=1260
coin_type = [500, 100, 50, 10]
count = 0

for coin in coin_type:
    count = count + n // coin
    n = n - (coin*(n//coin))  # n %= coin

print("최소 {}개의 동전이 필요합니다.".format(count))