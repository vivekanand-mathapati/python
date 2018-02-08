from functools import wraps

def new_decorator(func):
	
	@wraps(func)
	def wrap_func():
		print('i am in new_decorator')
		func()
		print('i am in new_decorator')

	return wrap_func

@new_decorator
def func_req_func():
	print('i am func_req_func')

# func_req_func = new_decorator(func_req_func)
func_req_func()
# print(help(func_req_func))