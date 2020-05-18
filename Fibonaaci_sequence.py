a=0
b=1
n=int(input("Enter number of terms of Fibonacci sequence: "))
if n==1:
	print(a)
elif n==2:
	print(a)
	print(b)
else:
	print(a)
	print(b)
	for i in range(n-2):
		temp=a
		a+=b
		b=temp
		print(a)
	
