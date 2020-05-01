# coding: utf-8

patoca = "パトカー"
tacusi = "タクシー"

i, j = 0, 0
str_list = []

for s in range(8):
    if s %2 == 0:
        str_list.append(patoca[i])
        i += 1
    else:
        str_list.append(tacusi[j])
        j += 1

result = "".join(str_list)
print(result)