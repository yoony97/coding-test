N = int(input())
string = [i for i in input()]
cnt = 0
for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if string[i] == "C" and string[j] == "O" and string[k] =="W":
                cnt +=1

print(cnt)
    