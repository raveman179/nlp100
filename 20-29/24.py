'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
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
# pprint(article)

filename = re.findall(r'''(?:ファイル):(.*?)\|''', article, re.MULTILINE)

pprint(filename)