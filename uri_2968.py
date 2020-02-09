import math

list = input().split(" ")

V,N = list

VN = int(V) * int(N)

v1 = math.ceil(VN * 0.1)

v2 = math.ceil(VN * (0.2))

v3 = math.ceil(VN * (0.3))

v4 = math.ceil(VN * (0.4))

v5 = math.ceil(VN * (0.5))

v6 = math.ceil(VN * (0.6))

v7 = math.ceil(VN * (0.7))

v8 = math.ceil(VN * (0.8))

v9 = math.ceil(VN * (0.9))

print("%i %i %i %i %i %i %i %i %i" % (v1,v2,v3,v4,v5,v6,v7,v8,v9))