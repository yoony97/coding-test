def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  
    r = 2 * i + 2  

    
    if l < n and arr[l] > arr[largest]:
        largest = l

    
    if r < n and arr[r] > arr[largest]:
        largest = r

    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  


def heap_sort(arr, n):
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0) 



n = int(input())
arr = list(map(int, input().split()))

heap_sort(arr, n)
print(' '.join([str(i) for i in arr] ))
