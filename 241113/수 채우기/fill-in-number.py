n = int(input())
min_coin = float('inf')
isfind = False
for i in range(n//5, 0, -1):
    target = n - i*5
    if target%2 == 0:
        min_coin = min(min_coin, i + target//2)
        print(min_coin)
        isfind = True
        break

if not isfind:
    print(-1)
