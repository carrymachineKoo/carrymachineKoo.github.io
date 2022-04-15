cnt=0
a=int(input())
arr=list(map(int,input().split()))
for i in arr:
	total=0
	if(i==1):
		total=1
	for j in range(2,i):	
		if(i%j==0):
			total=1		
	if(total==0): cnt+=1
print(cnt)