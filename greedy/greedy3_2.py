#큰 수의 법칙
# 1. 일단 입력받기
# 2. 입력받은 숫자 정렬하기
# 3. 가장 큰수 k번 더하기 -> m이 남았다면 -> 작은수 한번 더하기-> m이 남아있다면 반복


# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# max = data[n-1]
# second = data[n-2]
# result=0
#
# while m>0:
#     for i in range(k):
#         result += max
#         m -= 1
#         if m==0:
#             break
#
#     if m==0 :
#         break
#
#     result += second
#     m -= 1
#
# print (result)


# k개로 끊어지는걸 활용해서 해결해 볼수는 없을까?
# 1. k+1 짜리 수열 EX) 6665
# 2. (m // (k + 1))* k수열의 총합 + max * (m % (k + 1))

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
max = data[n-1]
second = data[n-2]
result=0

result = (m // (k+1)) * (k * max + second) + max * (m % (k + 1))

print (result)