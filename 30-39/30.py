'''
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''

import pandas as pd
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
    pprint(df_split)

text_to_dataframe("./nlp100/30-39/neko.txt.mecab")