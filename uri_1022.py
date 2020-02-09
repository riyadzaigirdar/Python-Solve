A,B,C,D = input().split(" ")

A = int(A)
B = int(B)
C = int(C)
D = int(D)

if(B>C and D>A and (C+D)>(A+B) and (abs(C) == C) and (abs(D) == D) and ((A%2) == 0) ):
    print("Valores aceitos")  
else:
    print("Valores nao aceitos") 

