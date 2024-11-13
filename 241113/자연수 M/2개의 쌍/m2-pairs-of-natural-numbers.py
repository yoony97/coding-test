from functools import cmp_to_key
from itertools import product
import sys

inputs = sys.stdin.read().strip().split("\n")

n = int(inputs[0])
numbers = []

for i in range(n):
    x, y= map(int, inputs[i+1].split())
    numbers.extend([y]*x)

numbers.sort()

offset = len(numbers)-1
li = []

for i in range(len(numbers)//2):
    print(numbers[i],numbers[offset])
    li.append(numbers[i] + numbers[offset])
    offset = offset -1

print(min(answer))