n = input()
li = list(map(int, input().split()))
li.sort()
print(' '.join([str(i) for i in li]))
print(' '.join([str(i) for i in li[::-1]]))