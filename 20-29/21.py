'''
21. カテゴリ名を含む行を抽出

記事中でカテゴリ名を宣言している行を抽出せよ．
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
pprint(re.findall(r'''^(\[\[Category:.*\]\].*)$''', article, re.MULTILINE))