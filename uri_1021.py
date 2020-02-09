N = float(input())


n1 = 0
n2 = 0
n3 = 0 
n4 = 0
n5 = 0 
n6 = 0
n7 = 0
n8 = 0
n9 = 0
n10 = 0
n11 = 0
n12 = 0

while(N >=100):
    n1 += 1
    N = N-100

while(N>=50):
    n2 += 1
    N = N-50    

while(N>=20):
    n3 += 1
    N = N-20

while(N>=10):
    n4 += 1
    N = N-10 

while(N>=5):
    n5 += 1
    N = N-5

while(N>=2):
    n6 += 1
    N = N-2

while(N>=1):
    n7 += 1
    N = N-1

while(N>=.50):
    n8 += 1
    N = N-.50

while(N>=.25):
    n9 += 1
    N = N-.25

while(N>=.10):
    n10 += 1
    N = N-.10

while(N>=.05):
    n11 += 1
    N = N-.05

while(N>=.01):
    n12 += 1
    N = N-.01

print("NOTAS:")
print("%i nota(s) de R$ 100.00" % n1)
print("%i nota(s) de R$ 50.00" % n2)
print("%i nota(s) de R$ 20.00" % n3)
print("%i nota(s) de R$ 10.00" % n4)
print("%i nota(s) de R$ 5.00" % n5)
print("%i nota(s) de R$ 2.00" % n6)


print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" % n7)
print("%i moeda(s) de R$ 0.50" % n8)
print("%i moeda(s) de R$ 0.25" % n9)
print("%i moeda(s) de R$ 0.10" % n10)
print("%i moeda(s) de R$ 0.05" % n11)
print("%i moeda(s) de R$ 0.01" % n12)


