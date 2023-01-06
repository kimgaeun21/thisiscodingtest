# 1이 될 때까지
# 1. n을 입력받아서 k의 배수가 될만큼 빼기
# 2. k로 나누기 n이 k보다 작을때 까지 반복
# 3. 나머지 수 1이 될때 까지 빼주기

n, k = map(int, input().split())
result = 0

while n >= k:
    if n % k == 0:
        n = n//k
        result += 1
    else :
        result += (n % k)
        n -= (n % k)

if n != 1:
    result += (n-1)

print (result)



