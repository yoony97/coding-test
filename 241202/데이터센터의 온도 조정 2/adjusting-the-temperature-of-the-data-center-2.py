N, C, G, H = map(int, input().split())  # N 장비개수, 작업량,
temps = []
for i in range(N):
    Ta, Tb = map(int, input().split())
    temps.append((Ta,Tb))

# A가 선호하는 온도  <  Ta  = C 작업
# Ta  <= A가 선호하는 온도 <= Tb   = G
#  A > Tb = H
def get_work(temp, Ta, Tb):
    if temp < Ta:
        return  C
    elif Ta <= temp <= Tb:
        return G
    else:
        return H

ans = 0
for temp in range(1001):
    total_work = 0
    for (Ta, Tb) in temps:
        total_work+= get_work(temp, Ta, Tb)
    ans =  max(ans, total_work)

print(ans )