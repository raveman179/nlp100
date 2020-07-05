'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを
可能な限り除去し，国の基本情報を整形せよ．
'''

import pandas as pd
import re
from pprint import pprint

def wiki_json_extract(keyword):
    '''
    extract keyword from wikipedia json format
    
    argus:  keywords to be extract
    return: Keyword extracted dataframes in json format
    '''
    df = pd.read_json('./20-29/jawiki-country.json.gz', lines=True)
    extract_keyword = df[df.title == keyword]['text'].values[0]
    return extract_keyword

def removal_markup(templates):
    '''
    remove markup 

    argus:template to be processed
    return:remove markup tags
    '''

    # 強調マークアップの除去
    template = {}
    for t_item in templates.items():
        template_extract = re.sub(r'\'{2,5}', '', t_item[1], re.MULTILINE+re.DOTALL)
        template[t_item[0]]=template_extract

    # 内部リンクの除去
    innerlink = {}
    for m_item in template.items():
        inner_extract = re.sub(r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]', r'\1', m_item[1],  re.MULTILINE+re.DOTALL)    
        innerlink[m_item[0]]=inner_extract

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

article = wiki_json_extract('イギリス')

basicinfo = re.findall(r'''^\{\{基礎情報.*?(.*?)^\}\}$''', article, re.MULTILINE+re.DOTALL)
temps = re.findall(r'''^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))''', basicinfo[0], re.MULTILINE+re.DOTALL)

templates = {temp[0]:temp[1] for temp in temps}

pprint(removal_markup(templates))