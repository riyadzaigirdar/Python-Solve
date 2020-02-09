N = int(input())

s = N%60

m1 = N/60

h=m1/60

m = m1%60

#print(f'{int(h)}:{int(m)}:{int(s)}')
print("%i:%i:%i" % (h,m,s))