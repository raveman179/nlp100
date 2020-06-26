import pandas as pd
import re

pd.set_option("display.max_colwidth", 200)
df = pd.read_csv('./20-29/eng_json.txt', delimiter='\n', header=None)

for index, row in df[0].iteritems():
    filename = re.findall(r'\[\[ファイル:([^|\]]*)', str(row))
    if filename != []:
        for x in filename:
            print(x)