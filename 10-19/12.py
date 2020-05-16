before = 'popular-names.txt'
col1 = 'col1.txt'
col2 = 'col2.txt'

col1 = open(col1, mode='w')
col2 = open(col2, mode='w')

with open(before) as f:
    for i in f:
        i = i.split(' ')
        col1.write(i[0]+'\n')
        col2.write(i[1]+'\n')

col1.close()
col2.close()
	        