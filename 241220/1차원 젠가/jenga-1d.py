import sys

data = sys.stdin.read().strip().split('\n')
N = int(data[0])
arr = list(map(int, data[1:N+1]))
ops = [tuple(map(int, i.split())) for i in data[N+1:]]

def remove(s,e):
    temp = []
    for i in range(s-1,e):
        arr[i] = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])

    return temp


for (s, e) in ops:
    arr = remove(s,e)

print(len(arr))
for i in arr:
    print(i)
print()


