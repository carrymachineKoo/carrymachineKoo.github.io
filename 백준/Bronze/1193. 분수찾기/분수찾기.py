n=int(input())
a=1
while True:
	if(n<=a):
		break
	n-=a
	a+=1
	
if(a%2==0):
	m=a-n+1
	print(str(n)+'/'+str(m))
else:
	m=a-n+1
	print(str(m)+'/'+str(n))
	
