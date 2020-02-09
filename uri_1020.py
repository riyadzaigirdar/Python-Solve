n = int(input())

y = n/365

d1 = n%365

m = d1/30

d = d1%30

print("%i ano(s)\n%i mes(es)\n%i dia(s)" % (y,m,d))