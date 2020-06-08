import pandas as pd

before = './10-19/popular-names.txt'
col1, col2 = './10-19/col1.txt', './10-19/col2.txt'

df = pd.read_csv('./10-19/popular-names.txt', delimiter='\t', header=None)

df.iloc[:, 0:1].to_csv(col1, header=False, index=False)
df.iloc[:, 1:2].to_csv(col2, header=False, index=False)
