''' reduce applies computation on entair list and return its result'''

from functools import reduce

lst = [1,2,3,4,5]
print(sum(lst))

#use of reduce 
result = reduce(lambda x, y: x+y, lst)
print(result)
