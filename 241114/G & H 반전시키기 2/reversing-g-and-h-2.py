n = int(input())
current = [i for i in input()] 
target = [i for i in input()]
answer = 0

for i in range(n-1, -1, -1):

    if current[i] != target[i]:
        for j in range(0, i+1):
            if current[j] == 'H':
                current[j] = 'G'
            else:
                current[j] = 'H'       
        answer += 1

print(answer)