def lcm_list(numbers):
    # 두 수의 최대공약수를 구하는 보조 함수
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    # 두 수의 최소공배수를 구하는 보조 함수
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    
    # 기저 조건: 리스트에 숫자가 1개만 있을 경우
    if len(numbers) == 1:
        return numbers[0]
    # 기저 조건: 리스트에 숫자가 2개 있을 경우
    if len(numbers) == 2:
        return lcm(numbers[0], numbers[1])
    
    # 재귀 호출: 첫 번째 수와 나머지 리스트의 최소공배수를 계산
    return lcm(numbers[0], lcm_list(numbers[1:]))

n = input()
li = list(map(int, input().split()))

print(lcm_list(li))