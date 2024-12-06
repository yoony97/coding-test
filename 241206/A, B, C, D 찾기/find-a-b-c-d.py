#A ≤ B ≤ C ≤ D 그리고 C ≤ A + B
inputs = list(map(int, input().split()))
inputs.sort()
A = inputs[0]
B = inputs[1]
C = inputs[2]
total = inputs[-1]

print(A, B, C, total - A - B - C)
