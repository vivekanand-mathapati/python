d = {}
print(type(d))
d = dict()
print(type(d))

d = {'vivek': 25, 'veer': 23, 'kiran': 22}
for key, value in d.items():
	print(key, value)

#or
for key in d:
	print(key, d[key])

d = dict([('vivek',25),('veer',23),('kumar',22)])
print(d.keys())
print(d.values())
