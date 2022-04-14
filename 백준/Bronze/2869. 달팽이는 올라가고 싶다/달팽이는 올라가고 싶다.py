import math
a,b,v=map(int,input().split())
c=a-b
print(math.ceil((v-a)/(a-b))+1)
