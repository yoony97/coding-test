#이때, 사진의 크기란 사진에서 양쪽 끝에 있는 사람 간의 거리로 정의되며, 사람이 1명 뿐인 경우에는 사진의 크기가 0입니다
li = [0]*(101)
N = int(input())
max_p = 0
for i in range(N):
    p, flag = input().split()
    li[int(p)] = flag
    max_p =  max(int(p), max_p)
    
max_dist = 0
li = li[:max_p+1]
#print(li)
for start in range(max_p+1):
    for end in range(start, max_p+1):
        H_cnt = 0
        G_cnt = 0
        isfirst = False
        s_idx =  0
        
        for i in range(start,end+1):
            if li[i] == "G":
                G_cnt += 1 
                
            elif li[i] == "H":
                H_cnt += 1
                
        if G_cnt != 0  and  H_cnt == 0:
            for s_idx in range(start, end+1):
                if li[s_idx] ==  'G':
                    break
            
            for e_idx in range(end, start-1, -1 ):
                if li[e_idx] ==  'G':
                    break
            
            dist = e_idx -  s_idx
            max_dist = max(max_dist, dist)

        if G_cnt == 0  and  H_cnt != 0:
            for s_idx in range(start, end+1):
                if li[s_idx] ==  'H':
                    break
            
            for e_idx in range(end, start-1, -1 ):
                if li[e_idx] ==  'H':
                    break
            
            
            dist = e_idx -  s_idx 
            max_dist = max(max_dist, dist)

        if G_cnt != 0 and H_cnt != 0 and G_cnt == H_cnt :
            for s_idx in range(start, end+1):
                if li[s_idx] !=  0:
                    break


            for e_idx in range(end, start-1, -1 ):
                if li[e_idx] !=  0:
                    break

            dist = e_idx -  s_idx
            max_dist = max(max_dist, dist)

print(max_dist)
