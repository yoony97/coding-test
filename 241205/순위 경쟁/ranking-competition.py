n = int(input())
li = []
current = [0,0,0]

def get_top(current):
    # C가 탑일 경우
    if current[2] > current[1] and current[2] > current[0]:
        return 0
    # B가 탑일 경우
    if current[1] > current[2] and current[1] > current[0]:
        return 1
    # A가 탑일 경우
    if current[0] > current[1] and current[0] > current[2]:
        return 2
    
    # A, B 가 공동 일 경우
    if current[0] == current[1] and  current[1] > current[2]:
        return 3
    # B, C 
    if current[1] == current[2] and  current[1] > current[0]:
        return 4
    # A, C 
    if current[0] == current[2] and  current[0] > current[1]:
        return 5
    # A, B, C

    if current[0] == current[1] == current[2]:
        return 6

prev = 2
ans = 0
for i in range(n):
    c, s = input().split()
    if c == 'A':
        current[0] += int(s)
    elif c == 'B':
        current[1] += int(s)
    else:
        current[2] += int(s)
    
    top = get_top(current)
    if prev != top: 
        ans += 1
    prev = top

print(ans)
    
