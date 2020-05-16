# coding: utf-8
import re
string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
restring = string.replace(',', '').replace('.', '')

str_list = restring.split()
result = [len(i) for i in str_list]
print(result)