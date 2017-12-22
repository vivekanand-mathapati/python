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

