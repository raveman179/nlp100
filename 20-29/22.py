import pandas as pd

df = pd.read_csv('./20-29/eng_json.txt', delimiter='\n', header=None)
category = df[0].str.extract("\[\[Category:(.+)\]\]").dropna(how='all')

print(category)
