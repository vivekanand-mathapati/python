<<<<<<< HEAD
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
=======
def square(val):
    return val*val

def add(val):
    return val + val

square_list = list(map(square,range(5)))
print(square_list)

#another use with lambda
lst = [1,2,3,4]
square_list = list(map(lambda x: x * x, lst))
print(square_list)

#another use of map on multiple functions 
funcs = [square,add]
for i in range(1,5):
    square_list = list(map(lambda x: x(i), funcs))
    print(square_list)

>>>>>>> b8d2e628c116f209ede07f95900115aa99583c4e
