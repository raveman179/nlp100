import pandas as pd
import math

split = int(input())
marge_ = './10-19/popular-names.txt'
output = ['output{}.txt'.format(i+1) for i in range(split)]

marge = pd.read_csv(marge_, header=None, delimiter='\t')
row = math.ceil(len(marge) / split)

filenum = 0 
txt_slice = [0, row]

while split > filenum:
    marge[txt_slice[0]:txt_slice[1]].to_csv(output[filenum], 
    header=False, index=False)
    txt_slice = list(map(lambda x: x + row, txt_slice))
    filenum += 1
