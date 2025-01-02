n = int(input())
numbers = list(map(int, input().split()))
total  = sum(numbers)
answer = float('inf')

def solve(cur_num, cnt, idx, current_val):
    global answer
    if cur_num == 2*n:
        if cnt == n:
            answer = min(answer, abs(total-current_val - current_val))
        return

    
    for i in range(idx, 2*n):
        #print(i, numbers[i])
        solve(cur_num+1, cnt+1, i+1, current_val + numbers[i]) #해당 숫자를 추가할 경우
        solve(cur_num+1, cnt, i+1, current_val) # 해당 숫자를 추가하지 않을 경우


solve(0, 0, 0, 0)
print(answer)