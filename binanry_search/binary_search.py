def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) //2
    if target < array[mid]:
        return binary_search(array, target, start, mid-1)
    elif target == array[mid]:
        return mid
    elif target > array[mid]:
        return binary_search(array, target, mid+1, end)

target = int(input())
array = list(map(int, input().split()))
array.sort()

result = binary_search(array, target, 0, len(array))

if result ==  False:
    print('target is not array')
else:
    print('target is at index {}'.format(result))