n, m = map(int, input().split())
array= list(map(int, input().split()))

result = 0
start =0
end = max(array)

def result_m(array, mid):
    total = 0
    for i in array:
        if  i > mid:
            total += (i-mid)
    return (total)

while start <= end:
    mid = (start + end)//2
   #  print(mid)
    x = result_m(array, mid)
    # print (x)
    if x > m :
        result = mid
        start = mid + 1
    elif x == m :
        result = mid
        break
    elif x < m :
        end = mid - 1

print (result)