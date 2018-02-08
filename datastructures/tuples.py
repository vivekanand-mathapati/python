t = ()
print(type(t))
t = tuple()
print(type(t))
t = 1,
print(type(t))

# t.append(6) tuples are immutable

t = ([1,2,3],[3,4,5]) # tuples van contain mutable
t[0][0] = 10
print(t)

# defining variables using tuples
t = 10,20,30 
a, b, c = t
print('a = {}, b = {}, c = {}'.format(a,b,c))