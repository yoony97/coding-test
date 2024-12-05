n = int(input())
li = []
current = [0,0]

def get_top(current):
    if current[0] <  current[1]:
        return 0 # B가 순위권
    elif current[0] >  current[1]:
        return  1 #  A가 순위권 
    else: 
        return 2 # 둘다

prev = 2
ans = 0
for i in range(n):
    c, s = input().split()
    if c == 'A':
        current[0] += int(s)
    else:
        current[1] += int(s)
    
    top = get_top(current)
    if prev != top: 
        ans += 1
    prev = top

print(ans)
    
