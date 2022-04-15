a,b=map(int,input().split())
if(a<b):
	temp=a
	a=b
	b=temp
def gcd(m,n):
	while(n>0):
		m,n=n,m%n
	return m
k=gcd(a,b)
print(k)
print(int(a*b/k))