"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
"""

target = input()
target = target.lower()
db = dict()
for s in target:
    if s not in list(db.keys()):
        db[s] = 0
    db[s] += 1
answer = ''
maximums = 0
maximum = 0
for key in db:
    if maximum < db[key]: 
        maximum = db[key]
        answer = key.upper()
        maximums = 0
    elif maximum == db[key]:
        #print(key)
        maximums += 1

if maximums == 0:
    print(answer)
else:
    print("?")