def max(a=input('first number: '),b=input('second number: '),c=input('third number: ')):
	if(a>b and a>c):
		l=a
	elif(b>a and b>c):
		l=b
	else:
		l=c
	return l
print('Largest number: ' ,max()) 
