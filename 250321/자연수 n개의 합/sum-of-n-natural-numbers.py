s = int(input())
psum = [0]*s
answer = 0 
for i in range(1, s):
    
    psum[i] = psum[i-1] + i
    if psum[i] > s:
        answer = i-1
        break
    if psum[i] == s:
        answer= i
        break
print(answer)
