# coding: utf-8
import re

string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.' 

restring = re.sub(r'[,\.]', '', string)
str_list = restring.split()

getfirstword = [1, 5, 6, 7, 8, 9, 15, 16, 19]
r_dict = {}
{r_dict.update({s[0]:i}) if i in getfirstword else r_dict.update({s[:2]:i}) for i, s in enumerate(str_list, 1)}

print(r_dict)
