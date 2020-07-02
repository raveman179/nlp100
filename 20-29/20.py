import pandas as pd
import re
from pprint import pprint

def wiki_json_extract(keyword):
    '''
    extract the keyword from wikipedia json format
    '''
    df = pd.read_json('./20-29/jawiki-country.json.gz', lines=True)
    keyword_df = df[df.title == keyword]['text'].values[0]
    return keyword_df

pprint(wiki_json_extract('イギリス'))


