s = {} #unlike other sets can not be created in this way
print(type(s))
s = set() # right way to create sets
print(type(s))

set_1 = {1,2,3,4}
# print(type(set_1))
print('set_1: ',set_1)
set_2 = {2,3,5,6,7}
print('set_2: ', set_2)
print('union: ', set_1 | set_2) #union of 2 sets
print('intersection: ', set_1 & set_2) #intersection of 2 sets
print('didderence: ', set_1 - set_2) #diff of 2 sets 
print('conjection: ', set_1 ^ set_2) #excludes common elements