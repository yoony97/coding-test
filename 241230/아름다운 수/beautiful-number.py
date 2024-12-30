from collections import Counter

N = int(input())
answer = []
answer_cnt = 0

def is_beautiful_number(number):
    num_str = ''.join([str(i)  for i in number])
    def helper(s, index):
        if index == len(s):
            return True
        current_char = s[index]
        count = int(current_char)
        end = index + count
        # 범위 초과 체크
        if end > len(s):
            #print(f"그룹 '{s[index:]}': 숫자 {current_char}이(가) {count}번 연속되지 않았습니다.")
            return False
        # 해당 그룹이 모두 동일한 숫자인지 확인
        if s[index:end] != current_char * count:
            #print(f"그룹 '{s[index:end]}'은(는) 숫자 {current_char}이(가) {count}번 연속되지 않았습니다.")
            return False
        # 다음 그룹으로 이동
        return helper(s, end)
    
    return helper(num_str, 0)


def choose(cur_num):
    global answer_cnt
    if cur_num == N:
        if is_beautiful_number(answer):
            answer_cnt+=1
            #print(answer)
        return
    
    for i in range(1, 5):
        answer.append(i)
        choose(cur_num+1)
        answer.pop()
    
choose(0)
print(answer_cnt)

        