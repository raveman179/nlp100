import pandas as pd

df = pd.read_csv('./20-29/eng_json.txt', delimiter='\n', header=None)
print(df[df[0].str.contains("\[\[Category:")])