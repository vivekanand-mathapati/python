#filter creates a list of elements for which a function returns true. Here is a short and concise example

def iseven(val):
    if val % 2 == 0:
        return True
    else:
        return False 

even_nums = list(filter(iseven,range(1,10)))
print(even_nums) 

#we can also achive this above functionality by using lambda

even_nums = list(filter(lambda x: x % 2 == 0, range(1,10)))
print(even_nums)

    
