n=int(input())
dp=[[0]*10 for i in range(101)]
dp[1]=[0,1,1,1,1,1,1,1,1,1]
#dp[2]=[1,1,2,2,2,2,2,2,2,1]
#dp[3]=[1,3,3,4,4,4,4,4,3,2]
for i in range(2,n+1):
	for j in range(0,10):
		if(j==0): dp[i][j]=dp[i-1][1]
		elif(1<=j<=8): dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
		elif(j==9): dp[i][j]=dp[i-1][8]
print(sum(dp[n])%1000000000)