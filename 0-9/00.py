# coding: utf-8

str_line = list("stressed")
reverse_list = []

for s in reversed(str_line):
    reverse_list.append(s)

result = "".join(reverse_list)
print(result)
