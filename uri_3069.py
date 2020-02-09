i = 0
j = 0
while(True):
    
    list1 = map(int,input().split(" "))

    if(list1[i] == 0 and list1[i+1] == 0):
        break

    while(True):
        list2 = map(int,input().split(" "))
        
        if(list2[j] < list2[j+1] and 0 <= list2[j] <= list1[i] and 0 <= list2[j+1] <= list1[i]):
            
            j+=2

        elif(list2[j]>list2[j+1]):
            list1[i+2]=list2.pop(j)
            list1[i+3]=list2.pop(j+1)
            i+=2
            continue
           
        elif(list2[j] == 0 and list2[j+1] == 0):
            break
        
    
    if(list2[j] == 0 and list2[j+1] == 0 ):
        break    
    i+=2