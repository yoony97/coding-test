import sys
input = sys.stdin.read

data = input().strip().split('\n')
elements = data[1:]
N, T = map(int, data[0].split(' '))
max_diff = 0
thres = 0
ava = []
for i in elements:
    i = int(i)
    if T - i >= 0:
        ava.append(i)
        
count = 0
result = T
for i in ava[::-1]:
    share = result//i
    if share >= 0:
        result -= share*i
        count += share
        
print(count)