A,B,C = input().split()

a = int(A)
b = int(B)
c = int(C)

maxab = ((a+b)+abs(a-b))/2
maxabc =((maxab+c)+abs(maxab-c))/2

print(int(maxabc),"eh o maior")