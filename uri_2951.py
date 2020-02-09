list = input().split()
N,G = list
N,G = int(N),int(G)
d={}
sum = 0

d = dict(input().split() for i in range(N))    

X = int(input())

runes = input().split() 

for i in range(X):
    for j in d:
        if (runes[i] == j):
            sum += int(d[j])
print(sum)
if(sum >= G):
    print("You shall pass!")
else:
    print("My precioooous")    