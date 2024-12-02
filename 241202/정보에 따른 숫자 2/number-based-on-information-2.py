T, A, B = map(int, input().split())
MAX_LEN = 1001
li = [0]*MAX_LEN
cnt = 0

for i in range(T):
    c, num = input().split()
    li[int(num)] = c
 
def find(target, current):
    left = 0
    right = MAX_LEN + 1
    for i in range(current, 0, -1):
        if li[i] == target:
            left = i
            break
    
    for j in range(current, MAX_LEN):
        if li[j] == target:
            right = j
            break

    return min(current - left, right-current)

for current in range(A,B+1):
    d1 = find('S', current)
    d2 = find('N', current)
    if d1 <= d2:
        #print(current, d1, d2)
        cnt += 1

print(cnt)
#print(li[A:B+1])
#가장 가까이에 있는 알파벳 N까지의 거리  =d2
#  가장 가까이에 있는 알파벳 S까지의 거리 d1
# d1 <= d2 일  경우, x=k는 특별한 위치
# k 개수 구하세요.
