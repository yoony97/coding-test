N, B = map(int, input().split())
students = []
for i in range(N):
    students.append(int(input()))

students.sort() # 싼 선물로 정렬

ans = 0
#한개를 정해서 반값 쿠폰을 쓰면 됨
for i in range(N): # i = 반값 쿠폰을 쓸 선물
    cnt = 1
    budget = B
    budget -= students[i]//2
    for j in range(N): # 
        if i == j:
            continue
        if budget - students[j] > 0:
            cnt +=1
            budget -= students[j]
        else:
            break
        ans = max(ans, cnt)

print(ans)