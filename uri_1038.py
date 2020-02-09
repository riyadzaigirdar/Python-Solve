X,Y = input().split(" ")

T = 0

if(X == "1"):
    T = float(Y)*4.00
    print("Total: R$ %.2f" % T)   
elif(X == "2"):
    T = float(Y)*4.50
    print("Total: R$ %.2f" % T)
elif(X == "3"):
    T = float(Y)*5.00
    print("Total: R$ %.2f" % T)
elif(X == "4"):
    T = float(Y)*2.00
    print("Total: R$ %.2f" % T)
elif(X == "5"):
    T = float(Y)*1.50
    print("Total: R$ %.2f" % T)        



