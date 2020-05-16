numofsplit = int(input())
marge = 'c1c2marge.txt'
output = ['output{}.txt'.format(i+1) for i in range(numofsplit)]

with open(marge, mode='r') as marge:
    split_list = marge.split('\n')

splittimes = len(split_list) / numofsplit

for i in lange(len(output)):
    with open(output[i+1], mode='w') as output[i+1]:
        