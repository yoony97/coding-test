#덧셈 뺼셈 곱셈
#연산자간의 우선순위 무시
#차례대로 계산함


minimum = float('inf')
maximum = float('-inf')

n = int(input())
numbers = list(map(int, input().split()))
count = list(map(int, input().split())) #[덧셈, 뺄샘, 곱셈] 개수

def back(cur_num, count, value, start):
    global maximum, minimum
    if cur_num == n: #연산을 n번 했다.
        minimum = min(value, minimum)
        maximum = max(value, maximum)
        return 
    
    for i in range(start+1, len(numbers)):
        
        if count[0] > 0:
            count[0]-=1
            back(cur_num+1, count, value + numbers[i], i)  
            count[0] += 1        

        if count[1] > 0:
            count[1]-=1
            back(cur_num+1, count, value - numbers[i], i)      
            count[1] += 1 
        
        if count[2] > 0:
            count[2]-=1
            back(cur_num+1, count, value * numbers[i], i)      
            count[2]+= 1        
        



for i in range(len(numbers)):
    used = [False]*len(numbers)
    used[i] = True
    back(1, count, numbers[i], i)

print(minimum, maximum)