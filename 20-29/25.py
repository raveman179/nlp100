'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と
値を抽出し，辞書オブジェクトとして格納せよ．
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
# print(article)

basicinfo = re.findall(r'''^\{\{基礎情報.*?(.*?)^\}\}$''', article, re.MULTILINE+re.DOTALL)
# print(basicinfo)

temp_extract = re.findall(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))''', basicinfo[0], re.MULTILINE+re.DOTALL)
pprint(temp_extract)