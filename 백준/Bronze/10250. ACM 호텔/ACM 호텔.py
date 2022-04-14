n=int(input())
for i in range(n):
	a,b,c=map(int,input().split())
	if(c%a!=0):
		print(100*(c%a)+(c//a+1))
	else:
		print(100*a+c//a)