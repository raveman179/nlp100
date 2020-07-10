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
    
    args: Keywords to be extracted
    return: 
    '''
    df = pd.read_json('./20-29/jawiki-country.json.gz', lines=True)
    extract_keyword = df[df.title == keyword]['text'].values[0]
    return extract_keyword

def basicinfo_perse():
    '''
    args:
    retrun:
    '''
    pass

article = wiki_json_extract('イギリス')
basicinfo = re.findall(r'''^\{\{基礎情報.*?(.*?)^\}\}$''', article, re.MULTILINE+re.DOTALL)
pprint(basicinfo)
print("------------------------------------------------------")
print(type(basicinfo))
print(len(basicinfo))
print("------------------------------------------------------")
temps = re.findall(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))''', basicinfo[0], re.MULTILINE+re.DOTALL)

template = {temp[0]:temp[1] for temp in temps}    
pprint(template)