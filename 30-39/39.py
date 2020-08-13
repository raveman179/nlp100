'''
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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

def zipf_graph(df):
    surface = df['surface'].value_counts()
    
    fig = plt.figure()
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel('ランク')
    plt.ylabel('出現頻度')

    plt.scatter(x=range(1, len(surface)+1), y=surface)

    fig.savefig("graph_39.png")

neko_df = text_to_dataframe("./nlp100/30-39/neko.txt.mecab")
zipf_graph(neko_df)