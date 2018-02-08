'''As the name suggests, 
   filter creates a list of elements for which a function returns true.'''
def odds(value):
	return True if value % 2 != 0 else False

lst = [1,2,3,4,5]
odd_num = [x for x in filter(odds, lst)]
print(odd_num)

#OR
odd_num = [x for x in filter(lambda x: x%2 != 0, lst)]
print(odd_num)

#OR
odd_num = [x for x in filter(lambda x: odds(x), lst)]
print(odd_num)