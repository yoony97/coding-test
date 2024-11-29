N = int(input())
li = list(map(int, input().split()))

cnt = 0
for start in range(N):
    for end in range(start, N):
        s = 0
        for i in range(start, end + 1):
            s += li[i]
        m = s / (end - start + 1)

        if s % (end - start + 1) == 0:  # 정수 여부 확인
            m = s // (end - start + 1)  # 정수로 변환
            if m in li:
                cnt += 1

print(cnt)
