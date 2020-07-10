'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
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

def filename_extract(article):
    '''
    Extract filename from wiki article

    args: Extracted article by keyword(str)
    return: filename(list)
    '''
    
    filename = re.findall(r'''(?:ファイル):(.*?)\|''', article, re.MULTILINE)
    return filename

article = wiki_json_extract('イギリス')
pprint(filename_extract(article))