import pandas as pd
import re

df = pd.read_json('./20-29/jawiki-country.json.gz', lines=True)
df_england = df.query('title=="イギリス"')['text'].values[0]
print(df_england)

# df.query()で条件に合致した行を抽出。今回はtitleに”イギリス”を含む物。
# valuesはnumpyのndarrayで添字を渡さないと中身がそのまま帰ってくるので注意。
path_w = './20-29/eng_json.txt'

with open(path_w, mode='w') as f:
    output = df_england.replace('<br />', '\n')
    f.write(output)


