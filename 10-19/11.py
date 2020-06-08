before = './10-19/popular-names.txt'
after = './10-19/popular-names_after.txt'

with open(before) as f:
		s = f.read()
		sp_line = s.replace('\t', ' ')
		
with open(after, mode='w') as f:
	f.write(sp_line)