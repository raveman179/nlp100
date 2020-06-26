import pandas as pd
import re

df = pd.read_csv('./20-29/eng_json.txt', delimiter='\n', header=None)
section = df[0].str.extractall("^=(.*)=$")

for index, row in section.iterrows():
    eq_count = int(row[0].count('=') / 2)
    print(re.sub(r'[=\ ]', '', row[0]) + ', ' + str(eq_count))
