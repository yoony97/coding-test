X, Y = map(int, input().split())
max_ans = 0
for i in range(X,Y+1): 
    max_ans = max(max_ans, sum([int(k) for k in str(i)])) 

print(max_ans)