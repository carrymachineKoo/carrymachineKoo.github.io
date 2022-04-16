m,n=map(int,input().split())
def count(a,b):
	if(a<b):
		return 0
	
	cnt=0
	while(a>=b):
		cnt+=a//b
		a//=b
	return cnt
two=count(m,2)-count(n,2)-count(m-n,2)
five=count(m,5)-count(n,5)-count(m-n,5)
print(min(two,five))
