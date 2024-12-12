item =  []
inputs = input()

def solution(inputs):
  s = [] 
  for i  in inputs:
    if i == '(':
      s.append('(')
    else:
      if len(s) == 0:
        return False
      s.pop()

  if len(s) != 0:
    return False
  return True

if solution(inputs):
    print("Yes")
else:
    print("No")