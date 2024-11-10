from sortedcontainers import SortedList

T = int(input())

def solve(N:int, li:list):
    for i in range(N):
        if i%2 == 0:
            temp = SortedList(li[:i+1])
            #print(i, temp, i//2)
            print(temp[i//2-1], end=' ')
        
    
    

for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))
    solve(N, li)
    print()