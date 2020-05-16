# coding: utf-8

str_line = "パタトクカシーー"

pata_list = list(str_line)
odd_str = []

for s in range(0, 7, 2):
    odd_str.append(pata_list[s])

result = "".join(odd_str)
print(result)