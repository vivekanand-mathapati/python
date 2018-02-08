'''map function applies a function on each elemnt of a container or list'''
def squire(value):
	return value ** 2

def multiply(value):
	return value * 2

lst = [1,2,3,4,5,6]
sqr_lst = [x for x in map(squire,lst)]
print(sqr_lst)

#same can be achived by using labda function
sqr_lst = [x for x in map(lambda x: x ** 2, lst)]
print(sqr_lst)

#same can be achived as follow
sqr_lst = [x for x in map(lambda x: squire(x), lst)]
print(sqr_lst)

# funcs = [squire, multiply]
# for item in lst:
# 	value = map(lambda x: x(item), funcs)
# 	print(value)