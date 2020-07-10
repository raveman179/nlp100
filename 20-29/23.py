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
    Extract the keyword from wikipedia json format
    
    args: The keywords you want to use for extraction(str)
    return: Extracted article by keyword(str)
    '''
    df = pd.read_json('./20-29/jawiki-country.json.gz', lines=True)
    extract_keyword = df[df.title == keyword]['text'].values[0]
    return extract_keyword

def count_eq(article):
    '''
    'eq' remove from section name

    args:Extracted article by keyword(str)
    '''
    section_pat = re.compile(r'''^(=*)(.*?)=*$''')
    section_list = article.split('\n')
    for s in section_list:
        if s.startswith('='):
            eq = section_pat.sub(r'\1', s)
            eq_count = eq.count('=')
            section_name = section_pat.sub(r'\2', s)
            print("{}, {}".format(section_name, eq_count)) 

article = wiki_json_extract('イギリス')
print(count_eq(article))
