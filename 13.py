col1, col2 = 'col1.txt', 'col2.txt'
collist =[]
marge = 'c1c2marge.txt'

with open(col1, mode='r') as col1:
    c1 = [i.strip() for i in col1.readlines()]

with open(col2, mode='r') as col2:
    c2 = [j.strip() for j in col2.readlines()]

with open(marge, mode='w') as marge:
    for (i, j) in zip(c1, c2):
        collist += [i+'\t', j+'\n']
    marge.write(''.join(collist))
    