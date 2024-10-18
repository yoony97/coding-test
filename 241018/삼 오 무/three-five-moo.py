n = int(input())

left = 1
right = 10**9
def get_count(target):
    return target - (target // 3 + target // 5 - target // 15)



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