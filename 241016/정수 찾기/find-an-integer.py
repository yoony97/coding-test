# b의 각 원소가 수열 a에 포함되는지 알아보는 프로그램을 작성하세요.
n = int(input())
arr1 = set(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

for elem in arr2:
    if elem in arr1:
        print(1)
    else:
        print(0)