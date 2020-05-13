before = 'popular-names.txt'
after = 'popular-names.txt'

with open(before) as f:
		s = f.read()
		sp_line = s.replace('	', ' ')
		
with open(after, mode='w') as f:
	f.write(sp_line)