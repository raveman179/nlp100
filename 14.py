times = input()
marge = 'c1c2marge.txt'

with open(marge, mode='r') as marge:
    line = marge.read()
    pline = line.split('\n')
    
for i in range(int(times)):
    print(pline[i])
