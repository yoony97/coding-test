a, b, c, d = map(int, input().split())

hour = c - a
temp = hour*60 - b
answer = temp + d
print(answer)