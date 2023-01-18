n = int(input())
array = list(map(int, input().split()))

warehouse=[0] * n

warehouse[0]= array[0]
warehouse[1]= max(array[0], array[1])

for i in range(2, n):
    warehouse[i] = max(array[i] + warehouse[i-2], warehouse[i-1])

print(warehouse[n-1])