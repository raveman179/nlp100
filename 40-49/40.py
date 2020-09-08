"""
40. 係り受け解析結果の読み込み（形態素)
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，
各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．

参照先:　https://qiita.com/yamaru/items/48dcc527f433c22e0af9

"""

import pandas as pd
from pprint import pprint
import re

class Morph:
    def __init__(self, line):
        """
        cabochaでパースした形態素の行を一行づつ加工して、
        クラス変数として読み込む。
        """
        surface, attribute = line.split('\t')
        attr = attribute.split(',')
        self.surface = surface
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]

# (0)        (1)    (2)           3           4            5               6             (7)         8           9     
#表層形     品詞, 品詞分類1,  品詞分類2,  品詞分類3,     活用型,         活用形,           原形,     読み,       発音
#'surface', 'pos', 'pos1',      'pos2',     'pos3',   'utilitarian', 'conjugated_form', 'base', 'reading', 'pronunciation'

filename = "40-49/ai.ja.txt.parsed"

sentences = []
morphs = []

with open(filename, mode='r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('*'):
            continue
        elif line != 'EOS\n':
            morphs.append(Morph(line))            
        else:
            sentences.append(morphs)
            morphs = []

for m in sentences[2]:
    print(vars(m))
    # print(type(m))
