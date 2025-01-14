n = int(input())
sequence = list(map(int, input().split()))
dp1 = [1]*n
dp2 = [1]*n
dp3 = [1]*n

#print(sequence)
for i in range(n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            #증가 수열일  때
            dp1[i] = max(dp1[i], dp1[j]+1)
            dp3[i] = max(dp3[i], dp1[j]+1, dp1[i])
        if sequence[i] < sequence[j]:
            #감소 수열일  때
            dp2[i] = max(dp2[i], dp2[j]+1)
            dp3[i] = max(dp3[i], dp1[j]+1, dp3[j]+1)
    #print(dp3)

print(max(max(dp1),  max(dp2), max(dp3)))
#DP3은 어떻게 정의하지?
#증가 일떈, DP1과  같다고 볼수 있지 
#감소 일땐, dp1[i] + 1 이 맞나?