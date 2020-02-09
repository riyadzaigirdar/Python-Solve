N = int(input())
list = []
j=0
for i in range(N):
    s = input()
    if(len(s) == 5):
        list.append("3")
    elif((s == "two") or (s[j]=="t" and s[j+1] == "w") or (s[j]=="t" and s[j+2] == "o") or (s[j+1]=="w" and s[j+2] == "o")):
        list.append("2")    
    else:
        list.append("1")    

for i in list:
    print(i)