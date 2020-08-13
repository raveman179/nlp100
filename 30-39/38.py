'''
38. ヒストグラムPermalink
単語の出現頻度のヒストグラムを描け．
ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pprint import pprint


def text_to_dataframe(filename):
    '''
    args: text want to convert into dataframe(text file)
    return: Morphological
    ly indexed text(pandas dataframe)
    '''
    df = pd.read_table(filename, header=None)
    df_split = pd.concat([df[0], df[1].str.split(',', expand=True)], axis=1).dropna()
    df_split.columns = ['surface', 'pos', 'pos1', 'pos2', 'pos3', 'utilitarian', 'conjugated_form', 'base', 'reading', 'pronunciation']
    #                    表層形     品詞, 品詞分類1,  品詞分類2,  品詞分類3,     活用型,         活用形,        原形,     読み,       発音
    dataframe = df_split.reset_index(drop=True)
    return dataframe

def words_frequency_hist(df):
    '''
    show Word histgram by matplot

    args: Morphologically indexed text(pandas dataframe)
    '''
    surface = df['surface'].value_counts()

    fig = plt.figure()
    plt.hist(surface, bins=20, range=(1,20))
    
    fig.savefig("graph_38.png")

neko_df = text_to_dataframe("./nlp100/30-39/neko.txt.mecab")
words_frequency_hist(neko_df)