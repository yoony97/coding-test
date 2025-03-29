#행의 개수 >= 열의 개수
  # 행에 대해서 정렬(빈도수가 적은 순서대로)
  # 횟수가 같을 경우, 작은 순
  # 정렬 수행시, 숫자와 빈도수 출력
# 행의 개수 < 열의 개수
  # 열에 대해서 정렬

# 행 길이 또는 열길이 >= 100 처음 100개 만 받음

arr = []
r, c, k = map(int, input().split())
for i in range(3):
    row = list(map(int, input().split()))
    arr.append(row)


def count(row):
    new_row = []
    result = []
    for i in list(set(row)):
        if i != 0:        
            b = row.count(i)
            new_row.append((b,i))

    new_row.sort(key = lambda x: (x[0], x[1]))

    for i in new_row:
        result.extend([i[1], i[0]])

    return result, len(result)

def transpose(arr):
    #list(*zip(i) for i in arr:
    return [ list(i)  for i in list(zip(*arr))]


def sorting(arr):
    new_arr = []
    temp = []
    max_len = 0 
    for i in arr[:100]: #100까지 제한
        i = i[:100] #제한
        new_row, length = count(i)
        max_len = max(max_len, length)
        temp.append(new_row)
    
    for t in temp:
        new_row = t 
        if len(t) <= max_len:
            new_row.extend([0]*(max_len - len(t)))
        new_arr.append(new_row)
    return new_arr

def simulation(arr):
    max_len = 0
    if len(arr) < len(arr[0]): #행의 크기가 열의 크기보다 크거나 같을 떄,
        arr = transpose(arr)
        arr = sorting(arr)
        arr = transpose(arr)
    else:
        arr= sorting(arr)

    return arr


answer = 0
#arr = simulation(arr)
while True:
    answer += 1
    if answer >= 100:
        print(-1)
        break

    arr = simulation(arr)
    if 0 <= r-1 < len(arr) and 0 <= c-1 < len(arr[0]):
        if arr[r-1][c-1] == k:
            print(answer)
            break
    


