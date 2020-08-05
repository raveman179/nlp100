'''
37. 「猫」と共起頻度の高い上位10語
「猫」とよく共起する（共起頻度が高い）10語と
その出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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

def extract_cat_article(df):
    #”猫”を含む文章をまるごと抽出する
    surface = df['surface'].to_list()
    # print(surface[0:10])
    cat_article = []

    for index, word in enumerate(surface):
        sentence_index = index
        if word == "猫":
            #”猫”を含む文章の開始位置を検索する。
            #↓空白記号がない場合の処理を考える
            # todo:"。"の位置をリストへ
            #       猫を含む文中の単語を辞書に追加。｛key 単語:value 出現回数｝
            #      1.前の文の"。"の位置まで文章を遡りながら単語を辞書に追加
            #      2."。"に到達したら”猫”の後の単語を順次辞書に追加
            #      3.keyに単語が存在する場合はvalue+=1、存在しない場合は辞書に追加
            while surface[sentence_index-1] != "\u3000" or surface[sentence_index-1] != "。":
                sentence_index -= 1
            article_pos = sentence_index

            #文章をリストに追加する
            while surface[article_pos] != "。":
                cat_article.append(surface[article_pos])
                article_pos += 1
            article_pos = 0

    return cat_article


neko_df = text_to_dataframe("./30-39/neko.txt.mecab")
print(extract_cat_article(neko_df))