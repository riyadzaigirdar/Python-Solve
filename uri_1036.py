import math

A,B,C = input().split(" ")

A,B,C = float(A),float(B),float(C)

D = (B*B) - (4*A*C)
R1,R2 = 0,0

if(A>0 and D>=0):
    D=math.sqrt(D)
    R1 = -B + D
    R1 = R1/(2*A) 
    print("R1 = %.5f" % R1)
    
    R2 = -B - D
    R2 = R2/(2*A) 
    print("R2 = %.5f" % R2)
else:
    print("Impossivel calcular")
