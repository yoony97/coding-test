expression = input()
answer = -1*(float('inf'))

# Write your code here!

def solve(cur, current, prev):
    global answer
    if cur == len(expression):
        answer = max(current, answer)
        return

    if expression[cur] not in ['-', '*', '+']:
        for i in range(1, 5):
            if prev == '-':
                solve(cur+1, current - i, prev)
            elif prev == '*':
                solve(cur+1, current*i, prev)
            elif prev ==  '+':
                solve(cur+1, current+i, prev)
            elif prev == None:
                solve(cur+1, i, prev)
         
    else:
        solve(cur+1, current, expression[cur])

solve(0, 0, None)
print(answer) 
