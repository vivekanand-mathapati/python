'''for statement calls iter() on the container object. The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. '''

class Reverse:
	'''this class is written to implement reverse iteration'''

	def __init__(self,data):
		self.data = data
		self.index = len(data)

	def __iter__(self):
		return self

	def __next__(self):
		if self.index == 0:
			raise StopIteration
		else:
			self.index -= 1
			return self.data[self.index]

name = 'VIVEK'
itr_obj = iter(name)
print(next(itr_obj)) #V
print(next(itr_obj)) #I
print(next(itr_obj)) #V
print(next(itr_obj)) #E
print(next(itr_obj)) #K
# print(next(itr_obj)) #StopIteration

rev_obj = Reverse('veer')
print(next(rev_obj)) #r
print(next(rev_obj)) #e
print(next(rev_obj)) #e
print(next(rev_obj)) #v
print(next(rev_obj)) #StopIteration