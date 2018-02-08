# try:
# 	f = open('reducer.py','r')
# except FileNotFoundError as e:
# 	print('file not found', e)
# else:
# 	print(f.read())
# finally:
# 	print('Done!')

with open('Employee.py','r') as f:
	f.seek(300)
	for line in f:
		print(line, end = '')

if f.closed:
	print('file closed')
