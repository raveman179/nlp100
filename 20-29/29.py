'''
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
'''
import pandas as pd
import re
from pprint import pprint
import requests

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

def highlight_markup_strip(templates):
    '''
    args: dict type template(dict)
    return: striped highlight markup template(dict)
    '''
    markup = {}

    for item in templates.items():
        markup_extract = re.sub(r'\'{2,5}', '', item[1], re.MULTILINE+re.DOTALL)
        markup[item[0]]=markup_extract
    
    return markup

def innerlink_markup_strip(highlights):
    '''
    args: dict type template(dict)
    return: striped innerlink markup template(dict)
    '''
    innerlink = {}

    for item in highlights.items():
        inner_extract = re.sub(r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]', r'\1', item[1],  re.MULTILINE+re.DOTALL)    
        innerlink[item[0]]=inner_extract
    
    return innerlink

def markup_strip_all(innerlink):
    '''
    remove markup 

    argus:template to be processed
    return:remove markup tags
    '''

    # <br>, <ref>タグ、{{0}}等 ''で置換する
    del_str = re.compile(r'''<.*?>|\{\{.\}\}''')
     
    # {{lang}}、標語 r'\2'でマッチ
    r2_match = re.compile(r'''\{\{(.*?\|){2}(.*?)\}\}''', re.MULTILINE+re.DOTALL)
    
    # {{}}の要素を''で置換する
    del_wavbrak = re.compile(r'''\{\{.*?\}\}''')

    # [[]]の最後の要素を抽出する
    brace_last = re.compile(r'''.*\|(.*?)\]\]''')

    # urlからIMF以下最後の要素を抽出する
    url_extract = re.compile(r'''(?:=.*?)?\[.*?(IMF\>.*?)\]$''')

    delmarkup = {}
    for temp_item in innerlink.items():
        strip_tag = del_str.sub('', temp_item[1])
        lang_extract = r2_match.sub(r'\2', strip_tag)
        brace_extract = del_wavbrak.sub('', lang_extract)
        wavbrak_extract = brace_last.sub(r'\1', brace_extract)
        extract_result = url_extract.sub(r'\1', wavbrak_extract)
        delmarkup[temp_item[0]]=extract_result

    return delmarkup

def call_imageinfo_api(filename):

    S = requests.Session()
    url = "https://commons.wikimedia.org/w/api.php"
    
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "iiprop": "url",
        "titles": "File:{}".format(filename)
    }

    R = S.get(url=url, params=params)
    data = R.json()
    print(data['query']['pages']['347935']['imageinfo'][0]['url'])
    
article = wiki_json_extract('イギリス')
info = basicinfo_perse(article)
templates = template_dict(info)
highlights = highlight_markup_strip(templates)
innerlink = innerlink_markup_strip(highlights)
extract_templates = markup_strip_all(innerlink)

call_imageinfo_api(extract_templates['国旗画像'])