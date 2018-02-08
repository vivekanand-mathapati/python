def squeres(lst):
	for x in lst:
		yield x ** 2

lst = [1,2,3,4]
sqr_lst = squeres(lst)
for x in sqr_lst:
	print(x)