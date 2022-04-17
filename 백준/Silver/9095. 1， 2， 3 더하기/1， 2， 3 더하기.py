n = int(input()) #테스트케이스 개수
d=[0]*11
d[1]=1
d[2]=2
d[3]=4
for j in range(n):
	a=int(input())
	for i in range(4,a+1):
		d[i]=d[i-1]+d[i-2]+d[i-3]
	print(d[a])