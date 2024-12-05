n = int(input())
li = list(map(int, input().split()))

numbers = sorted(list(set(li)))

if len(numbers) == 1:
    ans = -1
else:
    sec = numbers[1]
    sec_idx = li.index(sec)
    cnt = 0
    for i in li:
        if i == sec:
            cnt += 1
    if cnt > 1:
        ans = -1
    else:
        ans = sec_idx + 1 

print(ans)
    

