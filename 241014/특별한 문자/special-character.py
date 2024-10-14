s = input()

dic = {}
for i in s:
    if i in dic:
        dic[i] =+1
    else:
        dic[i] = 1

fail = True
for key, value in enumerate(dic):
    if value == 1:
        print(key)
        fail= False
        break

if fail:
    print("None")