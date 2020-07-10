'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
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

def categoryname_extract(article):
    '''
    args:wiki article include catecory name(str)
    return:category name(list)
    '''
    category_name = re.findall(r'''(\[\[Category\:.*?\]\])$''', article, re.MULTILINE)
    return category_name

article = wiki_json_extract('イギリス')
pprint(categoryname_extract(article))