arr=[31,28,31,30,31,30,31,31,30,31,30,31]
day=["SUN","MON","TUE","WED","THU","FRI","SAT"]
m,d=map(int,input().split())
total=0
for i in range(m-1):
	total+=arr[i]
total+=d
print(day[total%7])