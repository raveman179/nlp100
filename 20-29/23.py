'''
23. セクション構造
記事中に含まれるセクション名とそのレベル
（例えば”== セクション名 ==”なら1）を表示せよ．
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
# pprint(re.findall(r'''^=(.*?)=$''', article, re.MULTILINE))
section = re.findall(r'''^=(.*?)=$''', article, re.MULTILINE)

for i in section:
    eq_count = int(i.count('=') / 2)
    print(re.sub(r'[=\ ]', '', i) + ', ' + str(eq_count))
