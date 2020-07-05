'''
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの
内部リンクマークアップを除去し，テキストに変換せよ
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
basicinfo = re.findall(r'''^\{\{基礎情報.*?(.*?)^\}\}$''', article, re.MULTILINE+re.DOTALL)
temps = re.findall(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))''', basicinfo[0], re.MULTILINE+re.DOTALL)

templates = {temp[0]:temp[1] for temp in temps}
markup = {}

for item in templates.items():
    markup_extract = re.sub(r'\'{2,5}', '', item[1], re.MULTILINE+re.DOTALL)
    markup[item[0]]=markup_extract

innerlink = {}
for item in markup.items():
    inner_extract = re.sub(r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]', r'\1', item[1],  re.MULTILINE+re.DOTALL)    
    innerlink[item[0]]=inner_extract

pprint(innerlink)