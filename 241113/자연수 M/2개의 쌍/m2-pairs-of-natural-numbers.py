from functools import cmp_to_key
from itertools import product
import sys

inputs = sys.stdin.read().strip().split("\n")

n = int(inputs[0])
numbers = []

#여기서 메모리 에러가 발생해
for i in range(n):
    x, y= map(int, inputs[i+1].split())
    numbers.append((x,y))

numbers.sort(key = lambda x: x[1])
print(numbers[0][1] + numbers[-1][1])
# offset = len(numbers)-1
# min_value = float('inf')

# for i in range(len(numbers)//2):
#     #print(numbers[i],numbers[offset])
#     min_value = min(min_value, numbers[i] + numbers[offset])
#     offset = offset -1

# print(min_value)