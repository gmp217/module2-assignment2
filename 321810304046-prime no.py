def prime(n=int(input('Enter a number: '))):
	if n<=1:
		return False
	elif n==2:
		return True
	else:
		for i in (2,n//2):
			if(n%i==0):
				return False
			return True
if(prime()):
	print('Number is prime number')
else:
	print('Number is not prime number')