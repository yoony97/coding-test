n = int(input())

left = 1
right = 10**9//(3*5)
def get_count(target):
    count = 0
    for i in range(1, target+1):
        if i%3 == 0:
            count += 1
        if i%5 == 0:
            count += 1
        if i%15 == 0:
            count -= 1
        
    return target-count



while left <= right:
    mid = (left+right)//2
    #print(left, right, mid)
    if get_count(mid) > n:
        right = mid - 1
    elif get_count(mid) < n:
        left = mid + 1
    else:
        print(mid)
        break