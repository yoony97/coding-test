from collections import deque
N = int(input())
q = deque([(N, 0)])


while q:
    num, cnt = q.popleft()
    target = [num+1, num-1]
    if num  == 1:
        print(cnt)
        break
    if num%3 == 0:
        q.append((num//3, cnt+1))
        target.append(num//3)
    elif num%2 == 0:
        target.append(num//2)
        q.append((num//2, cnt+1))
    else:
        q.append((num-1, cnt+1))
    q.append((num+1, cnt+1))



# Write your code here!
