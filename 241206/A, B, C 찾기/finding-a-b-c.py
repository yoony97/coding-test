inputs = list(map(int, input().split()))
A = min(inputs)
total = max(inputs) # A + B + C
s2 = total - A # B+C

inputs.remove(A)
inputs.remove(total)
inputs.remove(s2)

inputs.sort()

B = inputs[0]
C = inputs[1]
print(A,B,C)

#B, C, A+B, C+A
