import pandas as pd
from pprint import pprint
import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def worddict(self):
        morphdict = {"surface":self.surface, "base":self.base, "pos":self.pos, "pos1":self.pos1}
        return morphdict

# (0)        (1)    (2)           3           4            5               6             (7)         8           9     
#表層形     品詞, 品詞分類1,  品詞分類2,  品詞分類3,     活用型,         活用形,           原形,     読み,       発音
#'surface', 'pos', 'pos1',      'pos2',     'pos3',   'utilitarian', 'conjugated_form', 'base', 'reading', 'pronunciation'

filename = "40-49/ai.ja.txt.parsed"
with open(filename, mode='r', encoding='utf-8') as f:
    blocks = f.read().split('EOS\n')

explain_list = blocks[2].split('\n')

morph_list = []
for word in explain_list:
    if word.startswith('*') or not word:
        continue
    else:    
        attr = re.split('\t|,', word)
        morph = Morph(attr[0], attr[7], attr[1], attr[2])
        line = morph.worddict()
        morph_list.append(line)

pprint(morph_list)