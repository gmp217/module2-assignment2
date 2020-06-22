def rev(s=input('Input string to reverse: ')):
	rs=''
	i=len(s)
	while i>0:
		rs+=s[i-1]
		i=i-1
	return rs
print('Reversed string: ',rev())
	