from functools import cmp_to_key
import sys
inputs = sys.stdin.read().strip().split("\n")
n = int(inputs[0])
li = list(map(int,inputs[1:]))

def compare(x,y):
    x = str(x)
    y = str(y)

    if int(x+y) > int(y+x):
        return -1
    
    if int(x+y) < int(y+x):
        return 1
        
    return 0

li.sort(key=cmp_to_key(compare))
print(''.join([str(i) for i in li]))