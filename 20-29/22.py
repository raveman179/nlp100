'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
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
    args: wiki article include catecory name(str)
    return: category name(list)
    '''
    category_name = re.findall(r'''(\[\[Category\:.*?\]\])$''', article, re.MULTILINE)
    return category_name

def categoryname_strip(article):
    '''
    args: category name(list)
    return: striped category name(list)
    '''
    category_name = [re.sub(r'''^\[\[Category:(.*?)(?:\|.*)?\]\]''', r'\1', s) for s in article]
    return category_name

article = wiki_json_extract('イギリス')
row = categoryname_extract(article)
pprint(categoryname_strip(row))

#^\[\[Category:(.*?)        [[Category:以降の任意の文字列0文字以上 
# (?:                       (?:でキャプチャ対象外の文字列を指定
# \|.*                      |以降の任意の文字列
# )?\]\]                    )?でキャプチャ対象外のグループ化を終了