n = int(input())
#2X5의 방법의 수는 {2X4방법수+1(2X1한개추가)}+{2X3방법수+2(1X2두개+2X1두개)}
d=[0]*10001
d[1]=1
d[2]=2
for i in range(3,n+1):
	d[i]=d[i-1]+d[i-2]
print(d[n]%10007)
