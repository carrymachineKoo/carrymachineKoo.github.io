n=int(input())
for i in range(1,n+1):
	a=n-i
	while(a>0):
		print(" ",end="")
		a-=1
	while(i>0):
		print("*",end="")
		i-=1
	print("")