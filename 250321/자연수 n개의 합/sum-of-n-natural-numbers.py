s = int(input())
psum = [0]*s

for i in range(1, s):
    
    psum[i] = psum[i-1] + i
    if psum[i] >= s:
        break

print(i-1)
