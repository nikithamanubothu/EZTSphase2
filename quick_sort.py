def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    less=[x for x in arr[1:] if x<=pivot]
    greater=[x for x in arr[1:] if x>pivot]
    return quick_sort(less)+[pivot]+quick_sort(greater)
b=[2,3,1,4]
q=quick_sort(b)
print(q)
    