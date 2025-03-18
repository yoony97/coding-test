#n개의 시당
#검사 팀장 - 검사 팀원
#한가게당 팀장은 오직 한명(필수), 팀원은 여러명
import math

n = int(input())
clients = list(map(int, input().split()))
n_leader, n_member = map(int, input().split())
answer = 0
for client in clients: #O(N)
    temp = client - n_leader
    answer += 1
    if temp > 0: #팀원이 필요해
        answer += math.ceil(temp/n_member)

print(answer)