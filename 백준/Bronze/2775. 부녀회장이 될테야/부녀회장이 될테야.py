num=int(input())
for i in range(num):
	k=int(input())
	n=int(input())
	#[1 2 3 4 5 6 7 ...]
	#[1 3 6 10 ...]
	
	arr=[x for x in range(1,n+1)]	
	for i in range(0,k):
		for j in range(1,n):
			arr[j]=arr[j-1]+arr[j]
	print(arr[n-1])