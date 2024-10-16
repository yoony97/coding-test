n = int(input())
arr1 = set(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

s = []
for elem in arr2:
    if elem in arr1:
        s.append('1')
    else:
        s.append('0')    

print(' '.join(s))