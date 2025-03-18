#n개의 시당
#검사 팀장 - 검사 팀원
#한가게당 팀장은 오직 한명(필수), 팀원은 여러명
n = int(input())
clients = list(map(int, input().split()))
n_leader, n_member = map(int, input().split())
answer = 0
for client in clients: #O(N)
    temp = client - n_leader
    answer += 1
    if temp > 0: #팀원이 필요해
        #팀원 수는 남은 고객 수를 n_member로 나눈 수의 upper
        temp2 = temp//n_member
        if temp%n_member > 0:
            temp2 += 1
        answer += temp2 

print(answer)