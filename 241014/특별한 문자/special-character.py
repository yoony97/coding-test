s = input()

dic = {}
for i in s:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

fail = True
for key in dic:    
    if dic[key] == 1:
        print(key)
        fail= False
        break

if fail:
    print("None")