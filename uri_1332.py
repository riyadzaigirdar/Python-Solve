N = int(input())
list = []
j=0
for i in range(N):
    s = input()
    if((s == "one") or (s[j]=="o" and s[j+1] == "n") or (s[j]=="o" and s[j+2] == "e") or (s[j+1]=="n" and s[j+2] == "e")):
        list.append("1")    
    if((s == "two") or (s[j]=="t" and s[j+1] == "w") or (s[j]=="t" and s[j+2] == "o") or (s[j+1]=="w" and s[j+2] == "o")):
        list.append("2")
    if((s == "three") or (s[j]=="t" and s[j+1] == "h" and s[j+2] == "r" and s[j+3] == "e") or (s[j]=="t" and s[j+1] == "h" and s[j+2] == "r" and s[j+4] == "e") or (s[j]=="t" and s[j+1] == "h" and s[j+3] == "e" and s[j+4] == "e") or (s[j]=="t" and s[j+2] == "r" and s[j+3] == "e" and s[j+4] == "e") or (s[j+1]=="h" and s[j+2] == "r" and s[j+3] == "e" and s[j+4] == "e")):
        list.append("3")
    if((s == "four") or (s[j]=="f" and s[j+1] == "o" and s[j+2] == "u") or (s[j]=="f" and s[j+2] == "u" and s[j+3] == "r") or (s[j]=="f" and s[j+1] == "o" and s[j+3] == "r") or (s[j+1]=="o" and s[j+2] == "u" and s[j+3] == "r")):
        list.append("4")
    if((s == "five") or (s[j]=="f" and s[j+1] == "i" and s[j+2] == "v") or (s[j]=="f" and s[j+2] == "v" and s[j+3] == "e") or (s[j]=="f" and s[j+1] == "i" and s[j+3] == "e") or (s[j+1]=="i" and s[j+2] == "v" and s[j+3] == "e")):
        list.append("5")
    if((s == "six") or (s[j]=="s" and s[j+1] == "i") or (s[j]=="s" and s[j+2] == "x") or (s[j+1]=="i" and s[j+2] == "x")):
        list.append("6")    
    if((s == "seven") or (s[j]=="s" and s[j+1] == "e" and s[j+2] == "v" and s[j+3] == "e") or (s[j]=="s" and s[j+1] == "e" and s[j+2] == "v" and s[j+4] == "n") or (s[j]=="s" and s[j+1] == "e" and s[j+3] == "v" and s[j+4] == "n") or (s[j]=="s" and s[j+2] == "v" and s[j+3] == "e" and s[j+4] == "n") or (s[j+1]=="e" and s[j+2] == "v" and s[j+3] == "e" and s[j+4] == "n")):
        list.append("7")
    if((s == "eight") or (s[j]=="e" and s[j+1] == "i" and s[j+2] == "g" and s[j+3] == "h") or (s[j]=="e" and s[j+1] == "i" and s[j+2] == "g" and s[j+4] == "t") or (s[j]=="e" and s[j+1] == "i" and s[j+3] == "h" and s[j+4] == "t") or (s[j]=="e" and s[j+2] == "g" and s[j+3] == "h" and s[j+4] == "t") or (s[j+1]=="i" and s[j+2] == "g" and s[j+3] == "h" and s[j+4] == "t")):
        list.append("8")
    if((s == "nine") or (s[j]=="n" and s[j+1] == "i" and s[j+2] == "n") or (s[j]=="n" and s[j+2] == "n" and s[j+3] == "e") or (s[j]=="n" and s[j+1] == "i" and s[j+3] == "e") or (s[j+1]=="i" and s[j+2] == "n" and s[j+3] == "e")):
        list.append("9")                            

for i in list:
    print(i)


    
