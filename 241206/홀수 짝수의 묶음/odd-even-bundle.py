N = int(input())
li = list(map(int, input().split()))
even = 0
odd = 0
for i in range(N):
    if li[i]%2 == 0:
        even += 1
    else:
        odd += 1

#짝 : 짝수 + 짝수, 홀수 + 홀수, 짝수
#홀 : 홀수 + 짝수, 홀수
cnt = 0
while True:
    if cnt%2 ==  0:
        if even:
            even -= 1
            cnt +=1
        elif odd >= 2:
            odd -= 2
            cnt +=1 
        else:
            if even > 0 or odd > 0:
                cnt -= 1
            break
    else:
        if odd:
            odd -= 1
            cnt += 1
        else:
            break
print(cnt)
        
        

