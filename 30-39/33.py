'''
33. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
'''
import MeCab
import pandas as pd
import re
from pprint import pprint

def text_to_dataframe(filename):
    df = pd.read_table(filename, header=None)
    df_split = pd.concat([df[0], df[1].str.split(',', expand=True)], axis=1).dropna()
    df_split.columns = ['surface', 'pos', 'pos1', 'pos2', 'pos3', 'utilitarian', 'conjugated_form', 'base', 'reading', 'pronunciation']
    #                    表層形     品詞, 品詞分類1,  品詞分類2,  品詞分類3,     活用型,         活用形,        原形,     読み,       発音
    return df_split
    
def A_to_B(dataframe):
    pass

# の　かつ　pos:助詞、pos1:連体化で前後が名詞のものを抽出
neko_df = text_to_dataframe("./30-39/neko.txt.mecab")
print(neko_df.query('pos == "動詞"'))

# print(A_to_B(neko_df))

