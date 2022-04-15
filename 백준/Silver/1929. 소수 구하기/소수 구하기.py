a,b=map(int,input().split())
for i in range(a,b+1):
	total=0
	if(i>1):
		for j in range(2,int(i**0.5)+1):   #약수의 대칭성 이용!!시간초과 해결
			if(i%j==0):
				total=1
				break
		if(total==0): print(i)