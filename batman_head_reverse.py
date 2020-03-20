s1 =''
l=6

for i in range(7,0,-1):
    s2 = ''
    for j in range(1,i+1):
        print(j , end='')
        if i == 7:
            s1 = s1 + str(j)
            s1 = s1.replace('7','')           
        else:
            s2 = s2 + str(j)
    if i < 7:
        for k in range(i,l):
            print(end=' ')
    
    if i > 5: 
        print(s1[::-1])     
    elif i<=5:
         print(s2[::-1])

    print()
    l+=1       
   
