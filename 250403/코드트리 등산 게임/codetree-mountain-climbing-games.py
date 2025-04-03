import sys
input = sys.stdin.readline

Q = int(input())
mountains = []

def lis_length_bs(nums):
    if not nums:
        return 0
    lis = []  # 현재까지의 후보 수열

    for num in nums:
        if not lis or num > lis[-1]:
            lis.append(num)
        else:
            # lis에서 num이 들어갈 자리를 이분 탐색으로 찾음
            left, right = 0, len(lis) - 1
            while left < right:
                mid = (left + right) // 2
                if lis[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            lis[left] = num
    return lis

for _ in range(Q):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 100:
        mountains = cmd[2:]
    elif cmd[0] == 200:
        mountains.append(cmd[1])
    elif cmd[0] == 300:
        if mountains:
            mountains.pop()
    elif cmd[0] == 400:
        m_index = cmd[1]
        no_cable = lis_length_bs(mountains[:m_index])
        cable = lis_length_bs(mountains)
        
        print((len(no_cable)-1 + len(cable))*1_000_000 + cable[-1])
                    
            

