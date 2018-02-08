def foo(a,b=10,c=20)->str:
    '''This function is to demonstrate default arguments.
    
    this is summery'''
    print(a,b,c)
    print('annotations: ',foo.__annotations__)

foo(5)
foo(10,20,30)
print('documentation: ',foo.__doc__)
