list = input().split(" ")
N,X,Y = list
N,X,Y=int(N),int(X),int(Y)
a=0

if(0 < N < 10000 and 0 < X, Y < 100):
   a = N/(X+Y)    
    
print("%.2f" % a)

