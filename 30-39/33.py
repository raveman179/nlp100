'''
33. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
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
    
def B_of_A(df):
    '''
    args: Morphologically indexed text(pandas dataframe)
    return: A noun phrase in which two nouns are joined by "の"(list)
    '''
    bofa_df = df.groupby(['surface', 'pos', 'pos1']).get_group(('の', '助詞', '連体化'))
    searchlist = list(bofa_df.query('surface == "の"' ).index)
    BofA_list = []
    for row in searchlist:
        if df.loc[row-1, ['pos']].item() == '名詞' and df.loc[row+1, ['pos']].item() == '名詞':
            sentence = str(df.loc[row-1, ['surface']].item() + df.loc[row, ['surface']].item() + df.loc[row+1, ['surface']].item())
            BofA_list.append(sentence)
    return BofA_list

# の　かつ　pos:助詞、pos1:連体化で前後が名詞のものを抽出
neko_df = text_to_dataframe("./30-39/neko.txt.mecab")
print(B_of_A(neko_df))
