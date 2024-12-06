N = int(input())
block = []
for i in range(N): 
    block.append(int(input()))

target = sum(block)//N

cnt= 0
for i in range(N):
    if block[i] > target:
        cnt += block[i]-target
    
print(cnt)