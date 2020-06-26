import pandas as pd

df = pd.read_table('./10-19/popular-names.txt', header=None)

for index, value in df[0].value_counts().iteritems():
    print(index, ':', value)