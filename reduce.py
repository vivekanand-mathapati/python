# Reduce is a really useful function for performing some computation on a list and returning the result. 
# It applies a rolling computation to sequential pairs of values in a list. For example, if you wanted to compute the product of a list of integers.

from functools import reduce
def product(x,y):
    return x * y

lst = [1,2,3,4,5]
lst_product = reduce(product, lst)
print(lst_product)

#another aproach to achive the same by using lambda expresion
lst_product = reduce(lambda x, y: x * y, lst)
print(lst_product)