n = float(input())
if n<0 or n>100:
    print("Fora de intervalo",end="\n")
else:
    if n<=25:
        print("Intervalo [0,25]",end="\n")
    if n>25 and n<=50:
        print("Intervalo (25,50]",end="\n")
    if n>50 and n<=75:
        print("Intervalo (50,75]",end="\n")
    if n>75:
        print("Intervalo (75,100]",end="\n")