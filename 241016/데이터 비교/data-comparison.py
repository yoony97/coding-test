n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

s = []
for i in range(m):
    if arr2[i] in arr1:
        s.append('1')
    else:
        s.append('0')

print(' '.join(s))