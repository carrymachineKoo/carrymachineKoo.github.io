import math
n=int(input())
n=math.factorial(n)
n=str(n)
n=n[::-1]
cnt=0
for i in n:
	if(i=='0'):
		cnt+=1
	else:
		print(cnt)
		quit()