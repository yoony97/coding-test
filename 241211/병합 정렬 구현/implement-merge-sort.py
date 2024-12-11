n = int(input())
arr = list(map(int, input().split()))

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, height):
    merge_arr = []
    i = low
    j = mid + 1
    
    while i <=mid and j <= height:
        if arr[i] <= arr[j]:
            merge_arr.append(arr[i])
            i += 1
        
        else:
            merge_arr.append(arr[j])
            j += 1
    
    while i <= mid:
        merge_arr.append(arr[i])
        i+=1
    
    while j <= height:
        merge_arr.append(arr[j])
        j+=1
    
    for i in range(len(merge_arr)):
        arr[i] = merge_arr[i]

merge_sort(arr, 0, n-1)
print(arr)