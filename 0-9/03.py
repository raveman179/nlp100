# coding: utf-8
import re
string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

drop_cp = re.sub(r'[,\.]', '', string)
print([len(i) for i in drop_cp.split()])