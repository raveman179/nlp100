import pandas as pd

col1, col2 = './10-19/col1.txt', './10-19/col2.txt'
marge = './10-19/c1c2marge.txt'

c1 = pd.read_csv(col1, header=None)
c2 = pd.read_csv(col2, header=None)
c1c2 = pd.concat([c1, c2], axis=1)

c1c2.to_csv(marge, header=False, index=False, sep='\t')