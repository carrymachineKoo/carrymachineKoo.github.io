import sys
n=int(input())
arr=[0]*10000 #포도주 배열
for _ in range(n):
	arr[_]=int(input())
dp=[0]*10000
dp[0]=arr[0]
dp[1]=arr[0]+arr[1]
dp[2]=max(dp[1],arr[0]+arr[2],arr[1]+arr[2])
for i in range(3,n):
	dp[i]=max(arr[i]+arr[i-1]+dp[i-3],arr[i]+dp[i-2],dp[i-1])
print(dp[n-1])