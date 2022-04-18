T=int(input())
#50 40 200  140 250
#30 100 120 210 260
arr=[[0]*100001 for _ in range(2)]
for _ in range(T):
	n=int(input())
	arr[0][:5]=map(int,input().split())
	arr[1][:5]=map(int,input().split())	
	arr[0][1]+=arr[1][0]
	arr[1][1]+=arr[0][0]
	for i in range(2,n):
		arr[0][i]+=max(max(arr[0][i-2],arr[1][i-2]),arr[1][i-1])
		arr[1][i]+=max(max(arr[0][i-2],arr[1][i-2]),arr[0][i-1])
	print(max(arr[0][n-1],arr[1][n-1]))

		
