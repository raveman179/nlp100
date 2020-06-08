import pandas as pd

marge = './10-19/popular-names.txt'
drop_dup= './10-19/drop_dup.txt'

df = pd.read_csv(marge, header=None, delimiter='\t')
df.drop_duplicates(0).to_csv(drop_dup, header=False, index=False, sep='\t')