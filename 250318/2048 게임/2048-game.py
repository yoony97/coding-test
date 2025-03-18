#움직이는 함수
#합치는 함수
#다시 정렬하는 함수

N = int(input())
maps = []
for _ in range(N):
    inputs = list(map(int, input().split()))
    maps.append(inputs)
#합친 후에 빈칸을 0으로 채움


def move_line(line): #얘는 무조건 왼쪽으로 합치는 함수임
  #num이  0이 아닌 것들 추출
	filtered = [num for num in line if num != 0]
	merged = []
	skip = False
	for i in range(len(filtered)):
		if skip:
			skip = False
			continue
		if i + 1 < len(filtered) and filtered[i] == filtered[i+1]: # 동일한 숫자가 연속으로 나올 때,
			#합친거에 넣고, 그 다음은 스킵하도록함
			merged.append(filtered[i]*2)
			skip = True
		else:
			merged.append(filtered[i])
	#나머지 빈칸은 0으로 넣음
	merged.extend([0]*(len(line) - len(merged)))
	return merged


#전치를 활용하여 move_up move_down을 구하는 데 나에게 좀 이해가 안된다.
def transpose(board):
	return [list(row) for row in zip(*board)]

def move_left(board):
	return [move_line(row) for row in board]

def move_right(board):
#	오른쪽으로 합칠려면, line을 리버스하면 되는 거 아닐까?
# 뒤집어서 오른쪽으로 합침
# 그리고 다시 뒤집으면 오른쪽 정렬 될듯
	return [list(reversed(move_line(list(reversed(row))))) for row in board]

def move_up(board):
	transposed = transpose(board)
	moved = [move_line(row) for row in transposed]
	return transpose(moved)
	
def move_down(board): #전치하고 오른쪽으로 합쳐야하니까 move_right 처럼 시행해야함
	transposed = transpose(board)
	moved = [list(reversed(move_line(list(reversed(row))))) for row in  transposed]
	return transpose(moved)


def simulation(arr, direct):
    if direct == 0:
        new_arr = move_up(arr)
        
    if direct == 1:
        new_arr = move_down(arr)
        
    if direct == 2:
        new_arr = move_left(arr)
    
    if direct == 3:
        new_arr = move_right(arr)
        
    return new_arr
    
#백트래킹 해야할듯?
#백트레킹 어떻게 할래?
#백트레킹 할려면, 아래처럼 결국 넣었다가 진행하고, 빼고
# up up up up up -> up up up up left 
#그럴려면 어떤 방법이 적합할까?
#4^5 * O(n^3)가 시간 복잡도네? 
#1024만큼 재귀 돌려야하긴해
answer = 0

def backtracking(hist):
    global answer 
    global maps
    if len(hist) == 5:
        new_arr = [[ i for i in maps[j]] for j in range(N)]
        for i in hist:
            new_arr = simulation(new_arr, i)
        answer = max(answer, max([max(i) for i in new_arr]))
        return
    else:
        for i in range(4):
            hist.append(i)
            backtracking(hist)
            hist.pop()


backtracking([])
print(answer)
