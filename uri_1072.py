N = int(input())

inner = 0
out = 0
n=0

for i in range(N):
    n=int(input())
    if(10<=n<=20):
        inner += 1
    else:
        out += 1  

print("%i in" % inner)
print("%i out" % out)