from urllib.request import urlopen

def test_connection():
	try: 
		with urlopen('https://www.google.co.in/') as response:
			print('Internet connection is working fine.')
	except: 
		print('oops! looks like you lost connection to internet.')

test_connection()