N,M = map(int, input().split(" "))
target = ['01'*4,'10'*4]
arr = []
def check(target, current):
    #print(target, current)
    bit = int(target,2)^int(current,2)
    #print(bin(bit).count('1'))
    return bin(bit).count('1')

for _ in range(N):
    s = input()
    s = s.replace('W','0')
    s = s.replace('B','1')
    arr.append(s)

answer = []
for i in range(0,N-7):
    for j in range(0,M-7):
        cnt = [0, 0]
        ws = 0
        bs = 1
        for k in arr[i:i+8]:
            wc = check(target[ws%2],k[j:j+8])
            bc = check(target[bs%2],k[j:j+8])
            cnt[0] = cnt[0] + wc
            cnt[1] = cnt[1] + bc
            ws += 1
            bs += 1    
            

        answer.extend(cnt)

print(min(answer))




