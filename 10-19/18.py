import pandas as pd

marge = './10-19/popular-names.txt'

df = pd.read_csv(marge, header=None, delimiter='\t')
df_s = df.sort_values(2, ascending=False)
print(df_s)