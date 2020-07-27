'''
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''

import MeCab
import pandas as pd
import numpy as np
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
    dataframe = df_split.reset_index(drop=True)
    return dataframe

def conjunction_of_nouns(df):
    '''
    args: Morphologically indexed text(pandas dataframe)
    return: conjunction of nouns(list)
    '''
    pos_df = df.loc[:, ['surface', 'pos']]
    
    con_list = []
    sentence = ""
    for index, item in pos_df.iterrows():
        if item['pos'] == "名詞":
            sentence += item['surface']
        elif item['pos'] != "名詞":
            sentence = ""
        else:
            con_list.append(sentence)

    #   if 次のposも名詞なら:
    #       変数sentence + surface
    #   else:
    #       sentenceをlistにappend()して次のループに
    #   
    return con_list



neko_df = text_to_dataframe("./30-39/neko.txt.mecab")
pprint(conjunction_of_nouns(neko_df))