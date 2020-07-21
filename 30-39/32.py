'''
32. 動詞の原形
動詞の原形をすべて抽出せよ．
'''

import MeCab
import pandas as pd
import re
from pprint import pprint

def text_to_dataframe(filename):
    '''
    args: text want to convert into dataframe(text file)
    return: Morphologically indexed text(pandas dataframe)
    '''
    df = pd.read_table(filename, header=None)
    df_split = pd.concat([df[0], df[1].str.split(',', expand=True)], axis=1).dropna()
    df_split.columns = ['surface', 'pos', 'pos1', 'pos2', 'pos3', 'utilitarian', 'conjugated_form', 'base', 'reading', 'pronunciation']
    #                    表層形     品詞, 品詞分類1,  品詞分類2,  品詞分類3,     活用型,         活用形,        原形,     読み,       発音
    return df_split

neko_df = text_to_dataframe("./30-39/neko.txt.mecab")
base_extract = neko_df.query('pos == "動詞"')
print(base_extract[['surface', 'base']])