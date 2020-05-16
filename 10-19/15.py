times = int(input())
marge = 'c1c2marge.txt'

with open(marge, mode='r') as marge:
    line = marge.read()
    pline = line.split('\n')
for i in range(times):
    print(pline[-times])
    if times ==0:
        break
    else:
        times -= 1