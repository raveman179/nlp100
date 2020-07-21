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
    Extract the keyword from wikipedia json format
    
    args: The keywords you want to use for extraction(str)
    return: Extracted article by keyword(str)
    '''
    df = pd.read_json('./20-29/jawiki-country.json.gz', lines=True)
    extract_keyword = df[df.title == keyword]['text'].values[0]
    return extract_keyword

def basicinfo_perse(article):
    '''
    args: Extracted article by keyword(str)
    return: Basicinfo template(list)
    '''
    basicinfo = re.findall(r'''^\{\{基礎情報.*?(.*?)^\}\}$''', article, re.MULTILINE+re.DOTALL)
    return basicinfo

def template_dict(basicinfo):
    '''
    args: Basicinfo template(list)
    return: A dictionary object that extracts field names and values from a template(dict)
    '''
    temps = re.findall(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))''', basicinfo[0], re.MULTILINE+re.DOTALL)
    template = {temp[0]:temp[1] for temp in temps}    
    return template

article = wiki_json_extract('イギリス')
info = basicinfo_perse(article)
# pprint(info)
pprint(template_dict(info))