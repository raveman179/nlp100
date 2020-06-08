import pandas as pd

rows = int(input())
marge = './10-19/popular-names.txt'

df = pd.read_csv(marge, header=None, delimiter='\t')

print(df.tail(rows))