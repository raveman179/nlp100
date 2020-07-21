'''
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
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
    dataframe = df_split.reset_index(drop=True)
    return dataframe

def conjunction_of_nouns(df):
    '''
    args: Morphologically indexed text(pandas dataframe)
    return: conjunction of nouns(list)
    '''
    

    # while posが名詞の時:
    #   if 次のposも名詞なら:
    #       surfaceを結合
    #   else:
    #       listにappendして次のループに
    
    pass



neko_df = text_to_dataframe("./30-39/neko.txt.mecab")