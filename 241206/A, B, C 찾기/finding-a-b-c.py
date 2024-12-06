inputs = list(map(int, input().split()))
A = min(inputs)
total = max(inputs) # A + B + C
s2 = total - A # B+C

inputs.remove(A)
inputs.remove(total)
inputs.remove(s2)

inputs.sort()

B = inputs[0]
C = total - A - B
print(A, B, C)
#B, C, A+B, C+A
