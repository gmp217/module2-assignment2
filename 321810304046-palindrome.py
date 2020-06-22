try:
	num=int(input("Enter a number:"))
except Exception as ValueError:
	print('Invalid input enter a integer')
else:
	temp=num
	rev=0
	while(num>0):
	   	dig=num%10
	   	rev=rev*10+dig
	   	num=num//10
	if(temp==rev):
		print('The number is palindrome')
	else:
		print('Not a palindrome')
finally:
	print('program executed')