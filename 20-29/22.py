'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''
import pandas as pd
import re
from pprint import pprint

def wiki_json_extract(keyword):
    '''
    extract keyword from wikipedia json format
    '''
    df = pd.read_json('./20-29/jawiki-country.json.gz', lines=True)
    extract_keyword = df[df.title == keyword]['text'].values[0]
    return extract_keyword

article = wiki_json_extract('イギリス')
pprint(re.findall(r'''^\[\[Category:(.*?)(?:\|.*)?\]\]''', article, re.MULTILINE))

#^\[\[Category:(.*?)        [[Category:以降の任意の文字列0文字以上 
# (?:                       (?:でキャプチャ対象外の文字列を指定
# \|.*                      |以降の任意の文字列
# )?\]\]                    )?でキャプチャ対象外のグループ化を終了