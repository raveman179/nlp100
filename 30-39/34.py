'''
34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
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
    dataframe = df_split.reset_index(drop=True)
    return dataframe

def conjunction_of_nouns(df):
    '''
    args: Morphologically indexed text(pandas dataframe)
    return: conjunction of nouns(list)
    '''
    pos_df = df.loc[:, ['surface', 'pos']].query('pos == "名詞"').reset_index()
    index_diff = pos_df['index'].diff()
    index_diff.name = 'diff'
    
    #名詞すべてを含むリスト
    nouns_list = pd.concat([pos_df, index_diff], axis=1).values.tolist()

    #結合する名詞の位置リスト
    connect_nouns = [n for n in nouns_list if n[3] == 1.0]

    connect_list = []
    for i, words in enumerate(connect_nouns, 1):
        # nouns_listとconnect_nounsの要素が一致する位置の添字
        index = nouns_list.index(words) 
        sentence = ""
        
        #nouns_list[1]~[最後の要素の一つ前]
        sentence = nouns_list[index-1][1]

        #nouns_list[-1]が連接の場合    
        if i == len(connect_nouns) and nouns_list[index][3] == 1.0:
            sentence = nouns_list[index-1][1] + nouns_list[index][1]
            connect_list.append(sentence)
            break

        #連節の処理
        count = 0
        while nouns_list[index+count][3] == 1.0:
            sentence += nouns_list[index+count][1]
            count += 1
        connect_list.append(sentence)

    return connect_list

neko_df = text_to_dataframe("./30-39/neko.txt.mecab")
pprint(conjunction_of_nouns(neko_df))