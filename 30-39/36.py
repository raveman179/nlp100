'''
36. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''
import matplotlib as mpl
mpl.use('tkagg')

import matplotlib.pyplot as plt
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
    dataframe = df_split.reset_index(drop=True)
    return dataframe

def words_frequency_bar(df):
    '''
    show Top 10 Word Frequency Bar Graphs by matplot

    args: Morphologically indexed text(pandas dataframe)
    return: none
    '''
    surface = df['surface'].value_counts().reset_index()
    # pprint(surface)
    
    words = surface.iloc[:10, 0].to_list()
    freq = surface.iloc[:10, 1].to_list()

    words_de = list(reversed(words))
    freq_de = list(reversed(freq))

    plt.bar(words_de, freq_de, tick_label = words_de)
    plt.show()


neko_df = text_to_dataframe("./30-39/neko.txt.mecab")
words_frequency_bar(neko_df)