# 2차원 배열만들고 i행 j열의 경우의 수는 i-1행의 0~j까지의 경우의 합이다
n=int(input())
dp=[[0]*10 for _ in range(1001)]
dp[1]=[1,1,1,1,1,1,1,1,1,1]  #길이 i에 일의자리숫자 j로 끝나는 오르막수 개수
#dp[2]=[1,2,3,4,5,6,7,8,9,10]
for i in range(2,n+1):
	for j in range(10):
		dp[i][j]=sum(dp[i-1][:j+1])
print(sum(dp[n])%10007)