def foo(var, *args, **kwargs):
	print(var)
	#unpacking args
	for item in args:
		print(item)

	#unpacking kwargs
	for key in kwargs: 
		print('key: {}, value: {}'.format(key, kwargs[key]))

	print(type(args)) #tuple
	print(type(kwargs)) #dict


foo('vivek', 'veer', 'shankar', vivek_age = 25, veer_age = 26)
#OR
foo('vivek', *('veer', 'shankar'), **{'vivek_age': 25, 'veer_age': 26}) 
