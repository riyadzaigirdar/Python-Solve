N = int(input())
list=[]


for i in range(N):
    l = []
    temp=0
    a=0
    b=0

    l = input().split()
     
    a=int(max(l))
    b=int(min(l))
    
    while((a%b) != 0):
        temp = b
        b = a%b
        a = temp  
    
    list.append(b)

           
for i in list:
    print(i)
    
        
