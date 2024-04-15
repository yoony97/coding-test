"""
문제
어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

입력
첫째 줄에 두 정수 min과 max가 주어진다.

출력
첫째 줄에 min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수의 개수를 출력한다.

제한
1 ≤ min ≤ 1,000,000,000,000
min ≤ max ≤ min + 1,000,000
"""
#1 2 3 5 6 7 10

def count_squarefrees(minimum, maximum):
    count = maximum - minimum + 1
    # 제곱ㄴㄴ수가 아닌 숫자를 체크할 배열 초기화
    not_square_free = [False] * count
    i = 2
    while i * i <= maximum:
        square = i * i
        # 최소 시작점 찾기 (minimum 이상에서 첫 번째로 나오는 i의 제곱의 배수)
        start = ((minimum + square - 1) // square) * square
        for j in range(start, maximum + 1, square):
            if not not_square_free[j - minimum]:
                not_square_free[j - minimum] = True
                count -= 1
        i += 1
    
    return count


# 사용 예
minimum, maximum = map(int, input().split())
print(count_squarefrees(minimum, maximum))
