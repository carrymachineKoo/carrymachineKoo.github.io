import math
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    print(math.lcm(b,c))
